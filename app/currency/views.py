from django.shortcuts import render
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm
from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        context['source_count'] = Source.objects.count()
        return context


def contact_us_table(request):
    context = {
        "contact_us_list": ContactUs.objects.all(),
    }
    return render(request, 'contactus_table.html', context=context)


def contact_us_list(request):
    context = {
        "contact_us_list": ContactUs.objects.all(),
    }
    return render(request, 'base.html', context=context)


def rate_table(request):
    context = {
        "rate_list": Rate.objects.all()
    }
    return render(request, 'rate_table.html', context=context)


class RateListView(generic.ListView):
    queryset = Rate.objects.all()
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
