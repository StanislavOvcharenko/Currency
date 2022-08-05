from django.shortcuts import render
# from django.http import HttpResponse
from currency.models import ContactUs, Rate


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
