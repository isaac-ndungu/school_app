from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('programmes/', views.programmes, name='programmes'),
    path('contact/', views.contact, name='contact'),
]