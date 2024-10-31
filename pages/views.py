from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.models import CustomUser
from accounts.forms import ProfileEditForm
from .forms import MeetingCreateForm, MeetingEditForm
from .models import Meeting

POSTS_PER_PAGE = 10


User = get_user_model()


class MeetingListView(ListView):
    model = Meeting
    template_name = 'meetings/meeting_list.html'
    context_object_name = 'meetings'

    def get_queryset(self):
        user = self.request.user
        return Meeting.objects.filter(host=user) | Meeting.objects.filter(participants=user)


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
        return get_object_or_404(Meeting, unique_code=unique_code)

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
