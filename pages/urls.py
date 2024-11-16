from django.urls import path
from . import views
from .views import (
    MeetingListView,
    MeetingDetailView,
    MeetingCreateView,
    MeetingUpdateView,
    MeetingDeleteView,
)

from django.conf import settings
from django.conf.urls.static import static

app_name = "pages"

urlpatterns = [
    path('meetings/', MeetingListView.as_view(), name="meeting_list"),
    path('pages/meetings/<uuid:unique_code>/', MeetingDetailView.as_view(), name="meeting_detail"),
    path('pages/meetings/create/', MeetingCreateView.as_view(), name="meeting_create"),
    path('pages/meetings/<uuid:unique_code>/update/', MeetingUpdateView.as_view(), name="meeting_update"),
    path('pages/meetings/<uuid:unique_code>/delete/', MeetingDeleteView.as_view(), name="meeting_delete"),
    path('join_meeting/', views.join_meeting_view, name="join_meeting"),

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
    # path(
    #     "pages/create_meeting/",
    #     views.create_meeting,
    #     name="create_meeting"
    # ),
    path(
        "pages/date_selection/",
        views.DateSelection.as_view(),
        name="date_selection"
    ),
    # path(
    #     "pages/meeting/<uuid:unique_code>/",
    #     views.read_meeting,
    #     name="meeting_detail"
    # ),
    #  path(
    #     "pages/meeting/edit/<uuid:unique_code>/",
    #     views.edit_meeting,
    #     name="edit_meeting"
    # ),
    # path(
    #     'pages/meeting/delete/<uuid:unique_code>/',
    #     views.delete_meeting,
    #     name='delete_meeting'
    # ),
    path(
        'pages/profile/<str:username>/',
        views.profile_view,
        name='profile'
    ),
    # path(
    #     'pages/schedule/',
    #     views.schedule_view,
    #     name='schedule'
    # ),
    path(
        'pages/schedule/',
        views.ScheduleView.as_view(),
        name='schedule'
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
