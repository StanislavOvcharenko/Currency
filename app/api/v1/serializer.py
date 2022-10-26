from rest_framework.serializers import ModelSerializer
from currency.models import Rate, Source, ContactUs


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'base_currency_type',
            'currency_type',
            'source',

        )


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'bank_avatar',
        )


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'email_to',
            'subject',
            'message',
        )
