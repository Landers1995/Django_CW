from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.management import call_command
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import Mailing, Client, Message


class HomePageView(TemplateView):
    template_name = "mailing/home.html"


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.add_mailing'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.user = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.change_mailing'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    #permission_required = 'mailing.view_mailing'

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     for product in context_data['product_list']:
    #         active_version = Version.objects.filter(product_name=product, indicates_current_version=True)
    #         if active_version:
    #             product.active_version = active_version.last().name_version
    #         else:
    #             product.active_version = 'Отсутствует'
    #     return context_data


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'mailing.delete_mailing'
    success_url = reverse_lazy('mailing:mailing_list')

# def product_detail(requests, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(requests, "product_detail.html", context)


class ContactsPageView(TemplateView):
    template_name = "mailing/contacts.html"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.user = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    permission_required = 'mailing.view_client'

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.user:
    #         return MailingForm
    #     if user.has_perm('mailing.can_edit_is_active'):
    #         return ProductModeratorForm
    #     raise PermissionDenied



# class ClientDetailView(DetailView):
#     model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.user = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'mailing.change_message'
    success_url = reverse_lazy('mailing:message_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


def toggle_activity_mailing(request, pk):
    mailing_item = get_object_or_404(Mailing, pk=pk)
    if mailing_item.is_active:
        mailing_item.is_active = False
    else:
        mailing_item.is_active = True

    mailing_item.save()

    return redirect(reverse('mailing:mailing_list'))


def toggle_activity_client(request, pk):
    client_item = get_object_or_404(Client, pk=pk)
    if client_item.is_active:
        client_item.is_active = False
    else:
        client_item.is_active = True

    client_item.save()

    return redirect(reverse('mailing:client_list'))


def call_custom_command(request, command_id: int):
    if request.method == 'POST':
        if command_id == 1:
            call_command('send_mail')
    return redirect(reverse('mailing:mailing_list'))
