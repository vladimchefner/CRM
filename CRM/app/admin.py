from django.contrib import admin
from .models import Client, Stuff, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'is_subscribe', 'chat_id')


@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'position')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'date', 'client_id', 'stuff_id')
    list_filter = ('type', 'status', 'date')
