from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

from currency.models import Rate, Source, ContactUs
from api.serializer import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.tasks import send_contactus_mail


class RatesViewSet(XLSXFileMixin, ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    renderer_classes = [JSONRenderer, XLSXRenderer]
    filename = 'my_export.xlsx'


class SourcesView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        send_contactus_mail.delay(self.request.data['email_to'], self.request.data['message'])
        return response


class ContactUsList(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ContactUsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
