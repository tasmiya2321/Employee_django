
from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'
# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'


urlpatterns = [
    path('', LoginView.as_view(template_name='Registration/login.html'), name='login'),
    path("home/", views.home, name="home"),
    path("employee/", views.employee, name="employee"),
    path("saveemployee/", views.saveemployee, name="saveemployee"),
    path('forgetpassword/', views.forgetpassword, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('change_password/', views.change_password, name='change_password'),
    path('Session_main/', views.Session_main, name='Session_main'),
]
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()

