from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pages"

urlpatterns = [
    path("pages/about/", views.AboutView.as_view(), name="about"),
    path("pages/rules/", views.RulesView.as_view(), name="rules"),
    path('pages/profile/<str:username>/', views.profile_view, name='profile'),
    path(
        'pages/edit/<str:username>/',
        views.edit_profile_view,
        name='edit_profile'),
    path("", views.HomePage.as_view(), name="index"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
