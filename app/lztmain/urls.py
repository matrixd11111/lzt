from django.urls import path

from .views import *

app_name = 'lztmain'

urlpatterns = [
    path('', main, name='index'),

    path('clients/', clients, name='clients'),
    path('clients_add/', clients_add, name='clients_add'),
    path('clients_statistics/', clients_statistics, name='clients_statistics'),

    path('orders_history/', orders_history, name='orders_history'),
    path('orders_add/', orders_add, name='orders_add'),
    path('orders_statistics/', orders_statistics, name='orders_statistics'),

    path('services/', services, name='services'),
    path('services_add/', services_add, name='services_add'),
    path('services_statistics/', services_statistics, name='services_statistics'),
]
