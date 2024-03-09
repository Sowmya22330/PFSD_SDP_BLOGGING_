from django.urls import path

from . import views
from .views import register_user

urlpatterns = [

    path('', views.home),
    path('signup/', views.signup),
    path('register_user/', views.register_user, name='register_user'),
    path('newuser/', views.newuser),
    path('steps/', views.steps),
    path('aboutus/', views.aboutus),
    path('main/', views.main),
    path('food/', views.food),
    path('travel/', views.travel),
    path('create/', views.create),
]
