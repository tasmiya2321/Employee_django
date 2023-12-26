from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

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
  
   #path("", views.login, name="login"),
    # path('forgetpassword/', views.forgetpassword, name='forget_password'),  # Add a comma here
    # path('reset_password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path("home/", views.home, name="home"),
   # path("email/", views.email, name="email"),
    #path("subject_email/", views.subject_email, name="subject_email"),
    path("", views.login, name="login"),
    path("employee/", views.employee, name="employee"),
    # path("saveemployee/",views.saveemployee, name="saveemployee"),
   # path('forgetpassword/', views.forgetpassword, name='forget_password'),   
    #path('reset_password/', views.reset_password, name='reset_password'),
    #path('home/', views.home, name='home')
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls"))

    # path('forgetpassword/', views.forgetpassword, name='forget_password'),  # Add a comma here
    # path('reset_password/', views.reset_password, name='reset_password')

]
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()


