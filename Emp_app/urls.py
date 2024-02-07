from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .views import admin_module
from .views import employee 



urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("home/", views.home, name="home"),
    path('employee/', views.employee, name='employee'),
    path('employee/<int:emp_id>/', views.employee, name='employee'),
    path("saveemployee/", views.saveemployee, name="saveemployee"),
    path('forgetpassword/', views.forgetpassword, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('admin_module/', admin_module, name='admin_module'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('change_password/', views.change_password, name='change_password'),
    path('Session_main/', views.Session_main, name='Session_main'),
    path('createpage/', views.CreatePage, name='createpage'),
    path('save_session/', views.save_session, name='save_session')
  
    
   
]
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()