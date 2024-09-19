from django.contrib import admin
from django.urls import path, include
# from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import ContactsPageView, MailingListView, MailingDetailView, MailingCreateView, \
    MailingUpdateView, MailingDeleteView, ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView, \
    MessageCreateView, MessageDeleteView, MessageUpdateView, MessageListView, MessageDetailView, toggle_activity_mailing, \
    call_custom_command, toggle_activity_client

app_name = MailingConfig.name

urlpatterns = [
    #path("", home, name="home"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing_create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing_edit/<int:pk>/", MailingUpdateView.as_view(), name="mailing_edit"),
    path("mailing_delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"),

    path("client_list/", ClientListView.as_view(), name="client_list"),
    #path("client/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),
    path("client_edit/<int:pk>/", ClientUpdateView.as_view(), name="client_edit"),
    path("client_delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),

    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path("message_edit/<int:pk>/", MessageUpdateView.as_view(), name="message_edit"),
    path("message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),

    path("activity/<int:pk>/mailing/", toggle_activity_mailing, name="toggle_activity_mailing"),
    path("activity/<int:pk>/client/", toggle_activity_client, name="toggle_activity_client"),
    path("command/<int:command_id>/call/", call_custom_command, name="call_custom_command"),

 ]
