from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Count
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView)
from django.urls import reverse

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserForm


POSTS_PER_PAGE = 10


User = get_user_model()


class AccountView(TemplateView):
    template_name = 'pages/account.html'


class AccountEdit(TemplateView):
    template_name = 'pages/edit_profile.html'

class OrganizationMeeting(TemplateView):
    template_name = 'pages/organization_meeting.html'


class CreateMeeting(TemplateView):
    template_name = 'pages/create_meeting.html'


class DateSelection(TemplateView):
    template_name = 'pages/date_selection.html'


class HomePage(TemplateView):
    template_name = 'pages/index.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def internal_server_error(request):
    return render(request, 'pages/500.html', status=404)


def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        'user': user
    }
    return render(request, 'pages/profile.html', context)


def edit_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('pages:profile', username=user.username)
    else:
        form = CustomUserForm(instance=user)

    context = {
        'form': form,
        'user': user
    }
    return render(request, 'pages/edit_profile.html', context)
