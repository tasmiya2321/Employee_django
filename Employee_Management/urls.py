"""
Definition of urls for Employee_Management.
"""


from django.urls import include, path
from django.contrib import admin




urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("Emp_app.urls")),
]
