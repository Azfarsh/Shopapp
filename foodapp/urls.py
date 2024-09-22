from django.urls import path
from . import views

urlpatterns = [
    path('', views.food, name='home'),
    path('track/', views.track, name='track'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product/', views.product, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search')
]
