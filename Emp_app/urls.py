# urls.py
from django.contrib import admin
from django.urls import path
from . import views

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/", views.employee, name="employee"),
    path("home/", views.home, name="home"),
    path('', views.index, name="index"),
    path("login/", views.userlogin, name="login"),
    path("login/", views.login, name="login"),  # Change the name to avoid conflicts
    path('forgetpassword/', views.forgetpassword, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password')
]

# Uncomment the following lines if you intend to use them
# from django.conf import settings
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()


