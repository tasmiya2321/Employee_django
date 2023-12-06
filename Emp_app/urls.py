# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#       # Uncomment the next line to enable the admin:
#     path('admin/', admin.site.urls),
#     # path('', views.index,name="index"),
#     # path("", views.login, name="login"),
#     # path("home/",views.home,name="home"),
       # path("employee/",views.employee,name="employee")




from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
      # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    # path("employee/", views.employee, name="employee"),
    path("home/",views.home,name="home"),
    #path('', views.index,name="index"),
    # path("", views.login, name="login"),
    # path('forgetpassword/', views.forgetpassword, name='forget_password')
]
# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()