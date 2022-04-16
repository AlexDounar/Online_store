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
    # path('spare-part/', views.SparePartDetailView.as_view(), name="spare-part-detail"),
    path('spare-part/new/', views.SparePartCreateView.as_view(), name= "part-create"),
    path('category/create/', views.NewCategory.as_view(), name= "new-category-create"),



]