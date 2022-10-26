import django_filters
from currency.models import Rate, Source, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('gte', 'lte'),
            'sale': ('gte', 'lte'),
            'source': ('exact',),
            'base_currency_type': ('exact',),
            'currency_type': ('exact',)

        }


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = {
            'source_url': ('exact',),
            'name': ('exact',),
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'email_to': ('exact',),
            'subject': ('exact',),
            'message': ('exact',),
        }
