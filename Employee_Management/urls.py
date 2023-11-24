"""
Definition of urls for Employee_Management.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("Emp_app.urls")),
]
