from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "pages"

urlpatterns = [

    path(
      'pages/code_introduction/',
       views.CodeOIntroduction.as_view(),
       name='code_introduction'
    ),
    path(
        "pages/about/",
        views.AboutView.as_view(),
        name="about"
    ),
    path(
        "pages/rules/",
        views.RulesView.as_view(),
        name="rules"
    ),
    path(
        "",
        views.HomePage.as_view(),
        name="index"
    ),
    path(
        "pages/create_meeting/",
        views.create_meeting,
        name="create_meeting"
    ),
    path(
        "pages/date_selection/",
        views.DateSelection.as_view(),
        name="date_selection"
    ),
    path(
        "pages/meeting/<uuid:unique_code>/",
        views.read_meeting,
        name="meeting_detail"
    ),
    path(
        'pages/meeting/delete/<uuid:unique_code>/',
        views.delete_meeting,
        name='delete_meeting'
    ),
    path(
        'pages/profile/<str:username>/',
        views.profile_view,
        name='profile'
    ),
    path(
        'pages/edit/<str:username>/',
        views.edit_profile_view,
        name='edit_profile'
    ),
    path(
        "",
        views.HomePage.as_view(),
        name="index"
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
