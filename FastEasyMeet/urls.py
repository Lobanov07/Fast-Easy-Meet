from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


handler404 = "pages.views.page_not_found"
handler500 = "pages.views.internal_server_error"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("pages.urls")),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:index'),
        ),
        name='registration',
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$',
                            serve,
                            {'document_root': settings.MEDIA_ROOT}),
                    re_path(r'^static/(?P<path>.*)$',
                            serve,
                            {'document_root': settings.STATIC_ROOT}),
    ]