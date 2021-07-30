from django.contrib import admin
from .models import Client, Stuff, Order
from django.conf import settings
import requests


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'is_subscribe', 'chat_id')


@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'position')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'status', 'date', 'client_id', 'stuff_id')
    list_filter = ('type', 'status', 'date')

    def save_model(self, request, obj, form, change):
        client = Client.objects.get(id=obj.client_id)
        if client.is_subscribe:
            msg = f'Ваша заявка {obj.status}'
            requests.get(f'https://api.telegram.org/bot{settings.TOKEN}/'
                         f'sendMessage?chat_id={client.chat_id}&text={msg}')

        super().save_model(request, obj, form, change)
