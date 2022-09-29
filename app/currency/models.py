from django.db import models
from currency.model_choices import CurrencyType


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    email_to = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=10_000)
    create = models.DateTimeField(auto_now_add=True)


def source_avatar(instance, filename):
    return 'source_avatar/{0}/{1}'.format(instance.id, filename)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    bank_avatar = models.FileField(upload_to=source_avatar, default='bank.jpeg')


class Rate(models.Model):
    base_currency_type = models.CharField(max_length=3, choices=CurrencyType.choices,
                                          default=CurrencyType.CURRENCY_TYPE_UAH)
    currency_type = models.CharField(max_length=3, choices=CurrencyType.choices, null=True)
    sale = models.DecimalField(max_digits=10, decimal_places=4)
    buy = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ResponseLog(models.Model):
    response_time = models.FloatField(max_length=10)
    request_method = models.CharField(max_length=12)
    query_params = models.CharField(max_length=20)
    ip = models.CharField(max_length=100)
