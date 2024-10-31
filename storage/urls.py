from django.shortcuts import render
from django.urls import path, include
from . import views



urlpatterns = [
    path('', render, kwargs={'template_name': 'index.html'}, name='start_page'),
    #path('boxes/', render, kwargs={'template_name': 'boxes.html'}, name='box_page'),
    path('boxes/', views.view_products, name='box_page'),
    path('faq/', render, kwargs={'template_name': 'faq.html'}, name='faq_page'),
    path('myrent/', render, kwargs={'template_name': 'my-rent.html'}, name='myrent_page')
]