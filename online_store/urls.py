from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'store-home'),
    path('about/', views.about, name='store-about'),
    path('contacts/', views.contacts, name='store-contact'),
    path('catalogue/', views.catalogue, name='store-catalogue'),
    path('login/', views.login, name='store-login'),
    path('search/', views.search, name='store-search'),
    path('delivery/', views.delivery, name='store-delivery'),


]