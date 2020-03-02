from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import auth
from django.urls import reverse
from .models import *
from .forms import *
from django.db import connection


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'lztmain/index.html', context)


def clients(request):
    _clients = Client.objects.all()
    context = {
        'title': 'Клиенты',
        'clients': clients,
    }
    return render(request, 'lztmain/clients.html', context)


def clients_add(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {
        'title': 'Добавление клиента',
        'form': form,
    }
    return render(request, 'lztmain/clients_add.html', context)


def clients_statistics(request):
    context = {
        'title': 'Статистика клиентов'
    }
    return render(request, 'lztmain/clients_statistics.html', context)


def orders_history(request):
    orders = ServiceOrders.objects.select_related().values(
        'service_id__service_name', 'material_id__material_name', 'material_of_service_cost', 'service_id__service_cod',
        'service_id__service_price', 'service_id__service_cod'
    )
    context = {
        'title': 'История заказов',
        'orders': orders,
    }
    return render(request, 'lztmain/orders_history.html', context)


def orders_add(request):
    form = OrdersForm()

    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {
        'title': 'Добавление заказа',
        'form': form,
    }
    return render(request, 'lztmain/orders_add.html', context)


def orders_statistics(request):
    context = {
        'title': 'Статистика заказов'
    }
    return render(request, 'lztmain/orders_statistics.html', context)


def services(request):
    service = MaterialForService.objects.select_related().values(
        'service_id__service_name', 'material_id__material_name', 'material_of_service_cost', 'service_id__service_cod',
        'service_id__service_price', 'service_id__service_cod'
    )

    context = {
        'title': 'Услуги',
        'service': service,
    }
    return render(request, 'lztmain/services.html', context)


def services_add(request):
    form = ServiceForm()

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {
        'title': 'Добавление услуги',
        'form': form
    }
    return render(request, 'lztmain/services_add.html', context)


def services_statistics(request):
    context = {
        'title': 'Статистика услуг'
    }
    return render(request, 'lztmain/services_statistics.html', context)


def stats(request):
    context = {
        'title': 'Статистика'
    }
    return render(request, 'lztmain/stats.html', context)


class SearchResultsView(ListView):
    model = Client
    template_name = 'lztmain/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(
            Q(name__icontains=query) | Q(surname__icontains=query)
        )
        return object_list


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if request.POST.get('next'):
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('main'))

    get_next = request.GET.get('next')
    context = {
        'title': 'Вход',
        'next': get_next
    }
    return render(request, 'lztmain/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
