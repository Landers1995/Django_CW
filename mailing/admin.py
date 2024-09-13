from django.contrib import admin
from mailing.models import Mailing, Client, Message, TryMailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'send_date', 'create_date', 'update_date', 'status', 'interval', 'end_date', 'is_active')
    list_filter = ('client', 'send_date', 'status', 'interval', 'is_active',)
    search_fields = ('client',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'second_name', 'third_name', 'comment')
    list_filter = ('email',)
    search_fields = ('first_name', 'second_name', 'third_name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(TryMailing)
class TryMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_try', 'status', 'response', 'mailing')
    list_filter = ('status', 'last_try',)
    search_fields = ('status',)
