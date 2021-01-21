from django.urls import path
from django.contrib.auth import views as authViews
from .views import *

urlpatterns = [
    path("register/", register, name='register'),
    path("profile/", profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]