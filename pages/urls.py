from django.urls import path
from . import views


app_name = "pages"

urlpatterns = [
    path("pages/about/", views.AboutView.as_view(), name="about"),
    path("pages/rules/", views.RulesView.as_view(), name="rules"),
    path("", views.HomePage.as_view(), name="index"),
    path("pages/account/", views.AccountView.as_view(), name="account"),
    path("pages/edit_profile/", views.AccountEdit.as_view(), name="edit_profile"),
    path("pages/organization_meeting/", views.OrganizationMeeting.as_view(), name="organization")
]
