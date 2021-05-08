from django.urls import path, include
import requests

from . import views



urlpatterns = [
    path( 'users/', views.UserDashboard ,name = 'user-dashboard-request'    )
]