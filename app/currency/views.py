# from django.shortcuts import render
from django.http import HttpResponse
from currency.models import ContactUs


def contact_us_list(request):
    contact_list = []
    for contact in ContactUs.objects.all():
        contact_string = f'id : {contact.id}, email_from : {contact.email_from}, email_to : {contact.email_to}, ' \
                         f'subject : {contact.subject}, message : {contact.message}, data : {contact.create} <br>'
        contact_list.append(contact_string)
    return HttpResponse(contact_list)
