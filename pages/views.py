from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.db.models import Q

from accounts.models import CustomUser
from accounts.forms import ProfileEditForm
from .forms import MeetingCreateForm, MeetingEditForm, ScheduleForm
from .models import Meeting, Schedule
from .utils import generate_possible_times, count_available_participants


POSTS_PER_PAGE = 10

User = get_user_model()


def generate_meeting_time(request, unique_code):
    meeting = get_object_or_404(Meeting, unique_code=unique_code)

    participants = meeting.participants.all()

    preferred_date = meeting.preferred_date

    schedules = {}
    for participant in participants:
        schedules[participant] = Schedule.objects.filter(user=participant)

    if not schedules:
        return JsonResponse({"status": "error", "message": "У участников нет расписания"})

    possible_times = generate_possible_times(preferred_date)

    best_time = None
    max_participants = 0

    for time in possible_times:
        available_participants = count_available_participants(time, schedules)
        if available_participants > max_participants:
            best_time = time
            max_participants = available_participants

    if best_time:
        meeting.date_time = best_time
        meeting.save()
        return JsonResponse({"status": "success", "best_time": best_time.strftime('%Y-%m-%d %H:%M:%S')})

    return JsonResponse({"status": "error", "message": "Не удалось найти подходящее время"})


class MeetingListView(ListView):
    model = Meeting
    template_name = 'meetings/meeting_list.html'
    context_object_name = 'meetings'
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        queryset = Meeting.objects.filter(Q(host=user) | Q(participants=user))

        host_filter = self.request.GET.get('host')
        if host_filter:
            queryset = queryset.filter(host__username__icontains=host_filter)

        title_filter = self.request.GET.get('title')
        if title_filter:
            queryset = queryset.filter(title__icontains=title_filter)

        return queryset


class MeetingDetailView(DetailView):
    model = Meeting
    template_name = "meetings/meeting_detail.html"
    context_object_name = "meeting"

    def get_object(self):
        unique_code = self.kwargs.get("unique_code")
        return get_object_or_404(Meeting, unique_code=unique_code)


class MeetingCreateView(CreateView):
    model = Meeting
    form_class = MeetingCreateForm
    template_name = "meetings/meeting_form.html"
    success_url = reverse_lazy("pages:meeting_list")

    def form_valid(self, form):
        form.instance.host = self.request.user
        form.instance.status = "Запланировано"
        response = super().form_valid(form)
        return redirect('pages:meeting_detail',
                        unique_code=form.instance.unique_code)


class MeetingUpdateView(UpdateView):
    model = Meeting
    form_class = MeetingEditForm
    template_name = "meetings/meeting_form.html"
    success_url = reverse_lazy("pages:meeting_list")

    def get_object(self):
        unique_code = self.kwargs.get("unique_code")
        meeting = get_object_or_404(Meeting, unique_code=unique_code)
        if meeting.host != self.request.user:
            raise Http404("Вы не можете редактировать чужую встречу.")
        return meeting


    def form_valid(self, form):
        meeting = form.save()

        return redirect('pages:meeting_detail',
                        unique_code=meeting.unique_code)


class MeetingDeleteView(DeleteView):
    model = Meeting
    template_name = "meetings/meeting_confirm_delete.html"
    success_url = reverse_lazy("pages:meeting_list")

    def get_object(self):
        unique_code = self.kwargs.get("unique_code")
        return get_object_or_404(Meeting, unique_code=unique_code)


def edit_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if user != request.user:
        raise Http404("Вы не можете редактировать чужой профиль.")

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES,
                               instance=user)
        if form.is_valid():
            form.save()
            return redirect('pages:profile', username=user.username)
    else:
        form = ProfileEditForm(instance=user)

    context = {
        'form': form,
        'user': user
    }
    return render(request, 'pages/edit_profile.html', context)


class MeetingDetail(TemplateView):
    template_name = 'pages/meeting_detail.html'


class DateSelection(TemplateView):
    template_name = 'pages/date_selection.html'


class HomePage(TemplateView):
    template_name = 'pages/index.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


class CodeOIntroduction(TemplateView):
    template_name = 'pages/code_introduction.html'


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'errors/403csrf.html', status=403)


def internal_server_error(request):
    return render(request, 'errors/500.html', status=500)


def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)

    user_meetings = user.meetings.all()
    context = {
        'user': user,
        'user_meetings': user_meetings
    }
    return render(request, 'pages/account.html', context)


def join_meeting_view(request):
    if request.method == "POST" and request.user.is_authenticated:
        unique_code = request.POST.get("meeting_code")
        if not unique_code:
            return JsonResponse({"success": False, "message": "Код встречи отсутствует."})

        meeting = Meeting.objects.filter(unique_code=unique_code).first()
        if meeting:
            meeting.participants.add(request.user)
            meeting.save()
            return JsonResponse({"success": True, "message": "Вы успешно присоединились к встрече."})
        else:
            return JsonResponse({"success": False, "message": "Неверный код встречи."})

    return JsonResponse({"success": False, "message": "Требуется авторизация для присоединения к встрече."})


@method_decorator(login_required, name='dispatch')
class ScheduleView(View):
    def get(self, request):

        user_meetings = Schedule.objects.filter(user=request.user).order_by('start_time')


        meetings_by_day = []
        current_day = None
        current_day_meetings = []

        for meeting in user_meetings:
            meeting_date = meeting.start_time.date()

            if current_day != meeting_date:
                if current_day is not None:
                    meetings_by_day.append((current_day, current_day_meetings))
                current_day = meeting_date
                current_day_meetings = [meeting]
            else:
                current_day_meetings.append(meeting)

        if current_day is not None:
            meetings_by_day.append((current_day, current_day_meetings))


        paginator = Paginator(meetings_by_day, 3)  
        page_number = request.GET.get('page')
        paginated_meetings = paginator.get_page(page_number)

        form = ScheduleForm()

        return render(request, 'pages/schedule.html', {
            'meetings_by_day': paginated_meetings,
            'form': form
        })

    def post(self, request):
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new_schedule = form.save(commit=False)
            new_schedule.user = request.user
            new_schedule.save()
            return redirect('pages:schedule')
        return render(request, 'pages/schedule.html', {'form': form})
