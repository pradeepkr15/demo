from django.urls import path
from adminApp import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.userLogout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.userProfile, name='profile'),
    path('student/', views.student, name='student'),
    path('blank-page/', views.blank_page, name='blank_page'),
]