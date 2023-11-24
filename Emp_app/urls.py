from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', views.index),
    path("", views.login, name="login")
]
