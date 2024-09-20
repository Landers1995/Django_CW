from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from mailing.forms import MailingForm, ClientForm, MessageForm
from blog.models import Blog
from mailing.models import Mailing, Client
from random import sample


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['mailing_list'] = Mailing.objects.all().count()
        context_data['mailing_list_active'] = Mailing.objects.all().filter(is_active=True).count()
        context_data['client_list'] = Client.objects.all().count()
        context_data['blog_list'] = Blog.objects.all().order_by('?')[:3]
        return context_data


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object
