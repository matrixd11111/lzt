from django.db import models
from django.utils.timezone import now


# Create your models here.

class Performer(models.Model):
    """описание таблицы Исполнитель"""

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    performer_name = models.CharField(verbose_name='Исполнитель', max_length=64)
    performer_note = models.TextField(verbose_name='Примечание', max_length=64, blank=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.performer_name


class Client(models.Model):
    """описание таблицы Клиент"""

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='имя')
    surname = models.CharField(max_length=64, verbose_name='фамилия')
    third_name = models.CharField(max_length=64, verbose_name='отчество')
    birth_date = models.DateField(verbose_name='Дата рождения', auto_now_add=False, blank=True)
    phone_number = models.CharField(verbose_name='Телефон', max_length=12, blank=True)
    note = models.TextField(verbose_name='Примечание', max_length=64, blank=True)
    email = models.EmailField(verbose_name='e-mail', max_length=64, blank=True)
    patient = models.BooleanField(verbose_name='Пациент', blank=True)
    client_type = models.ForeignKey('ClientType', on_delete=models.CASCADE, verbose_name='Тип клиента', blank=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.name


class ClientType(models.Model):
    """описание таблицы Тип Клиента"""

    class Meta:
        verbose_name = 'Тип Клиента'
        verbose_name_plural = 'Типы Клиентов'

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Тип клиента', max_length=64)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    """описание таблицы Услуги"""

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['service_cod']

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    service_cod = models.CharField(verbose_name='Код услуги', max_length=10, unique=True)
    service_name = models.CharField(verbose_name='Название услуги', max_length=255)
    service_note = models.CharField(verbose_name='Примечание', max_length=255, blank=True)
    service_price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2,
                                        blank=True, default='0')
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.service_name


class Material(models.Model):
    """описание таблицы Расходные материалы Услуги"""

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['material_name']

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    material_name = models.CharField(verbose_name='Название Материала', max_length=255)
    material_note = models.CharField(verbose_name='Примечание Материала', max_length=255, blank=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.material_name


class MaterialForService(models.Model):
    """описание таблицы Расходные материалы Услуги"""

    class Meta:
        verbose_name = 'Материал для Услуги'
        verbose_name_plural = 'Материалы для Услуг'
        ordering = ['pk']

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    material_id = models.ForeignKey(Material, verbose_name='Материал', on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.CASCADE)
    material_of_service_cost = models.DecimalField(verbose_name='Количество', max_digits=12, decimal_places=2,
                                                   blank=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return "{} / {}".format(self.material_id.material_name, self.material_of_service_cost)


class Orders(models.Model):
    """описание таблицы Заказов"""

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=False, auto_now=True, blank=True)
    order_service = models.ForeignKey('ServiceOrders', verbose_name='Услуги', on_delete=models.CASCADE, blank=True)
    order_performer = models.ForeignKey('Performer', verbose_name="Исполнитель", on_delete=models.CASCADE, blank=True)
    order_note = models.CharField(verbose_name='Примечание', max_length=255, blank=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return "{}".format(self.pk)


class ServiceOrders(models.Model):
    """описание таблицы Услуги для Заказа"""

    class Meta:
        verbose_name = 'Услуга для Заказа'
        verbose_name_plural = 'Услуги для Заказа'
        ordering = ['pk']

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    service_of_orders = models.ForeignKey(Service, verbose_name='Услуга для заказа',
                                          on_delete=models.CASCADE)
    service_cost_of_orders = models.DecimalField(verbose_name='Количество', max_digits=12, decimal_places=2,
                                                 blank=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', default=now)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return "{} / {}.шт.".format(self.service_of_orders.service_name, self.service_cost_of_orders)

# class MaterialForServiceCostOnDate(models.Model):
#     """описание таблицы цена Услуги на дату"""
#     pass
#
#
# class MaterialForServiceBalanceOnDate(models.Model):
#     """описание таблицы Остаток материала на дату"""
#     pass
#
#
# class Unit(models.Model):
#     """описание таблицы """
#     pass
#
#
# class ServiceCost(models.Model):
#     """описание таблицы Цена услуги"""
#     pass
#
#
# class OrdersHistory(models.Model):
#     """описание таблицы Истории заказов"""
#     pass
#
#
# class Organization(models.Model):
#     """описание таблицы Организация"""
#     pass
#
#
# class ServiceType(models.Model):
#     """описание таблицы Тип Услуги"""
#     pass
