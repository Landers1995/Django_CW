from django.contrib import admin
from mailing.models import Mailing


# @admin.register(Mailing)
# class MailingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'client', 'message', 'send_date', 'create_date', 'update_date', 'status', 'interval', 'end_date', 'is_active')
#     list_filter = ('client', 'send_date', 'status', 'interval', 'is_active')
#     search_fields = ('client',)
