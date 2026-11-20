from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('about/contacts/', views.contacts_view, name='contacts'),
    path('about/find-us/', views.find_us_view, name='find_us'),
    path('concerts/', views.concerts_view, name='concerts'),
    path('orchestra/', views.orchestra_view, name='orchestra'),
]