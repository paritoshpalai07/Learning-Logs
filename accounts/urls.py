from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('sign-up/', views.UserSignUp, name='signup')
]