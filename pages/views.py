from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Count
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView)
from django.urls import reverse

# from .forms import PostForm, CommentForm
#from .models import Post, Category, Comment


class HomePage(TemplateView):
    template_name = 'pages/index.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


class AccountView(TemplateView):
    template_name = 'pages/account.html'

<<<<<<< HEAD

class AccountEdit(TemplateView):
    template_name = 'pages/edit_profile.html'

=======
class JointomeetView(TemplateView):
    template_name = 'pages/meetjoin.html'
>>>>>>> 36be28adea375df06d55a89f2b4959625ad19df1

def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def internal_server_error(request):
    return render(request, 'pages/500.html', status=404)


POSTS_PER_PAGE = 10


User = get_user_model()




#class PostListMixin(ListView):
    #paginate_by = POSTS_PER_PAGE


