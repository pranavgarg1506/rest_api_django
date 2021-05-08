from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('register/',   views.register_request ,name = 'register-request' ),
    path('login/',   views.login_request ,name = 'login-request' ),
    #path('profile/', views.profile_request, name='profile-request'),
    path('logout/', views.logout_request, name='logout-request'),
    path('', views.home_request, name='home-request'),

    path('api/', include(router.urls)),





]