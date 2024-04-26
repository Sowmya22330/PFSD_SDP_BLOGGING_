from django.urls import path

from . import views
from .views import register_user

urlpatterns = [

    path('', views.home),
    path('signin_view/', views.signin_view, name='signin_view'),
    path('signup/', views.signup),
    path('register_user/', views.register_user, name='register_user'),
    path('newuser/', views.newuser),
    path('steps/', views.steps),
    path('aboutus/', views.aboutus),
    path('main/<str:username>/', views.main, name='main'),
    path('food/', views.food),
    path('travel/', views.travel),
    path('new/<str:username>/', views.new, name='new'),
    path('allblogs/<str:username>/', views.allblogs),
    path('create/', views.create),
    path('trending/', views.trending),

    path('yourblogs/', views.yourblogs),
    path('feedback/<str:username>/', views.feedback_view, name='feedback'),
    path('admin login/', views.adminlogin),
    path('adminblogs/', views.adminblogs, name='adminblogs'),
]
