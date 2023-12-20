from django.contrib import admin
from django.urls import path
from . import views
#from . import ResetPasswordView
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/", views.employee, name="employee"),
    path("home/", views.home, name="home"),
    path('', views.index, name="index"),
    path("", views.login, name="login"),
    path('forgetpassword/', views.forgetpassword, name='forget_password'),  # Add a comma here
    path('reset_password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),
         name='reset_password_confirm'),
    path("email/", views.email, name="email"),
    path("subject_email/", views.subject_email, name="subject_email")
]

# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()