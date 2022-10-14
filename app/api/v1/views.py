from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

from api.v1.filters import RateFilter, SourceFilter, ContactUsFilter
from api.v1.pagination import RatePagination
from api.v1.throttles import AnonCurrencyThrottle
from currency.models import Rate, Source, ContactUs
from api.v1.serializer import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.tasks import send_contactus_mail
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class RatesViewSet(XLSXFileMixin, ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    renderer_classes = [JSONRenderer, XLSXRenderer]
    filename = 'my_export.xlsx'
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter)
    ordering_fields = ['id', 'buy', 'sale']
    throttle_classes = [AnonCurrencyThrottle]


class SourcesView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filterset_class = SourceFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter)
    ordering_fields = ['source_url', 'name']


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
    filterset_class = ContactUsFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter)
    ordering_fields = ['email_to', 'subject', 'message']
    search_fields = ['email_to', 'subject', 'message']


class ContactUsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
