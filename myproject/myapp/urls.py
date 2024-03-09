from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('signup/', views.signup),
    path('newuser/', views.newuser),
    path('steps/', views.steps),
    path('aboutus/', views.aboutus),
    path('main/', views.main),
]
