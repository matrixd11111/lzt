from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from lztmain.views import SearchResultsView

import lztmain.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path('clients/', mainapp.clients, name='clients'),
    path('stats/', mainapp.stats, name='stats'),
    path('clients_add/', mainapp.clients_add, name='clients_add'),
    path('clients_statistics/', mainapp.clients_statistics, name='clients_statistics'),
    path('orders_history/', mainapp.orders_history, name='orders_history'),
    path('orders_add/', mainapp.orders_add, name='orders_add'),
    path('orders_statistics/', mainapp.orders_statistics, name='orders_statistics'),
    path('services/', mainapp.services, name='services'),
    path('services_add/', mainapp.services_add, name='services_add'),
    path('services_statistics/', mainapp.services_statistics, name='services_statistics'),
    path('login/', mainapp.login, name='login'),
    path('logout/', mainapp.logout, name='logout'),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
