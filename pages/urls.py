from django.urls import path
from . import views


app_name = "pages"

urlpatterns = [
    path("pages/about/", views.AboutView.as_view(), name="about"),
    path("pages/rules/", views.RulesView.as_view(), name="rules"),
    path("", views.HomePage.as_view(), name="index"),
    path("pages/account/", views.AccountView.as_view(), name="account"),
<<<<<<< HEAD
    path("pages/edit_profile/", views.AccountEdit.as_view(), name="edit_profile")
=======
    path("pages/meetjoin/", views.JointomeetView.as_view(), name="meetjoin")
>>>>>>> 36be28adea375df06d55a89f2b4959625ad19df1
]
