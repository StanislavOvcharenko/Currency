from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm


def index(request):
    return render(request, 'index.html')


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


def rate_list(request):
    context = {
        "rate_list": Rate.objects.all()
    }
    return render(request, 'rate_list.html', context=context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {'form': form}
    return render(request, 'rate_create.html', context=context)


def rate_update(request, rate_id):

    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate_instance)

    context = {'form': form}
    return render(request, 'rate_update.html', context=context)


def rate_details(request, rate_id):
    rate_instance = get_object_or_404(Rate, id=rate_id)
    context = {'instance': rate_instance}
    return render(request, 'rate_details.html', context=context)


def rate_delete(request, rate_id):
    rate_instance = get_object_or_404(Rate, id=rate_id)
    context = {'instance': rate_instance}
    if request.method == 'POST':
        rate_instance.delete()
        return HttpResponseRedirect('/rate/list/')
    return render(request, 'rate_delete.html', context=context)


def source(request):
    context = {
        "source_list": Source.objects.all()
    }
    return render(request, 'source_list.html', context=context)


def source_create(request):
    if request.method == 'POST':
        source_form = SourceForm(request.POST)
        if source_form.is_valid():
            source_form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        source_form = SourceForm()

    context = {'source_form': source_form}
    return render(request, 'source_create.html', context=context)


def source_update(request, source_id):

    source_instance = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        source_form = SourceForm(request.POST, instance=source_instance)
        if source_form.is_valid():
            source_form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        source_form = SourceForm(instance=source_instance)

    context = {'source_form': source_form}
    return render(request, 'source_update.html', context=context)


def source_details(request, source_id):
    source_instance = get_object_or_404(Source, id=source_id)
    context = {'source_instance': source_instance}
    return render(request, 'source_details.html', context=context)


def source_delete(request, source_id):
    source_instance = get_object_or_404(Source, id=source_id)
    context = {'instance': source_instance}
    if request.method == 'POST':
        source_instance.delete()
        return HttpResponseRedirect('/source/list/')
    return render(request, 'source_delete.html', context=context)
