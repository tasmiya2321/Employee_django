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
handler502 = 'myapp.views.custom_502_view'

urlpatterns = [
  
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("home/", views.home, name="home"),
    path("employee/", views.employee, name="employee"),
    path("saveemployee/",views.saveemployee, name="saveemployee"),
    path('forgetpassword/', views.forgetpassword, name='forget_password'),  
    path('reset_password/', views.reset_password, name='reset_password'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path("createpage", views.CreatePage, name='createpage')
    

    # path('forgetpassword/', views.forgetpassword, name='forget_password'),  # Add a comma here
    # path('reset_password/', views.reset_password, name='reset_password')

]
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()


