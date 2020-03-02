from django.contrib import admin
from .models import *


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'third_name', 'birth_date', 'phone_number', 'email', 'patient', 'client_type',)
    search_fields = ('name', 'phone_number', 'email',)


class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_create', 'date_update')
    search_fields = ('pk',)


class MaterialForServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'material_id', 'service_id', 'date_create', 'date_update',)
    search_fields = ('pk', 'material_id',)


class PerformerAdmin(admin.ModelAdmin):
    list_display = ('performer_name',)
    search_fields = ('performer_name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_cod', 'service_name',)
    search_fields = ('service_name',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order_date', 'order_performer', 'order_note',)
    search_fields = ('pk',)


class ServiceForOrdersAdmin(admin.ModelAdmin):
    list_display = ('service_of_orders', 'service_cost_of_orders',)
    search_fields = ('service_of_orders',)


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientType, ClientTypeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialForService, MaterialForServiceAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(ServiceOrders, ServiceForOrdersAdmin)
