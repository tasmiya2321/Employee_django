from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/", views.employee, name="employee"),
    path("home/", views.home, name="home"),
    path('', views.index, name="index"),
    path("", views.login, name="login"),
    path('forgetpassword/', views.forgetpassword, name='forget_password'),  # Add a comma here
    path('reset_password/', views.reset_password, name='reset_password')
]
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()