from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import Mailing, Client, Message


class HomePageView(TemplateView):
    template_name = "mailing/home.html"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    # def form_valid(self, form):
    #     # form.instance.creator = self.request.user
    #     # return super().form_valid()
    #
    #     product = form.save()
    #     user = self.request.user
    #     product.creator = user
    #     product.save()
    #     return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = ProductFormset(instance=self.object)
    #     return context_data
    #
    # def form_valid(self, form):
    #     context_data = self.get_context_data()
    #     formset = context_data['formset']
    #     if form.is_valid() and formset.is_valid():
    #         self.object = form.save()
    #         formset.instance = self.object
    #         formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, formset=formset))
    #
    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.creator:
    #         return ProductForm
    #     if user.has_perm('catalog.can_edit_description') and user.has_perm('catalog.can_edit_category') and user.has_perm('catalog.can_edit_is_publication'):
    #         return ProductModeratorForm
    #     raise PermissionDenied


class MailingListView(ListView):
    model = Mailing

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     for product in context_data['product_list']:
    #         active_version = Version.objects.filter(product_name=product, indicates_current_version=True)
    #         if active_version:
    #             product.active_version = active_version.last().name_version
    #         else:
    #             product.active_version = 'Отсутствует'
    #     return context_data


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

# def product_detail(requests, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(requests, "product_detail.html", context)


class ContactsPageView(TemplateView):
    template_name = "mailing/contacts.html"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientListView(ListView):
    model = Client


# class ClientDetailView(DetailView):
#     model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
