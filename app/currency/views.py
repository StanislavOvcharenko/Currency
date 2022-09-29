# from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm, ContactusForm
from django.views import generic
from django.urls import reverse_lazy

from currency.tasks import send_contactus_mail


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        context['source_count'] = Source.objects.count()
        return context


class ContactUsView(generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class ContactUsCreateView(generic.CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_create.html'
    form_class = ContactusForm
    success_url = reverse_lazy('currency:contactus_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        send_contactus_mail.delay(self.object.email_to, self.object.message)

        return response


class RateListView(LoginRequiredMixin, generic.ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateDetailsView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


class SourceListView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDetailsView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user
