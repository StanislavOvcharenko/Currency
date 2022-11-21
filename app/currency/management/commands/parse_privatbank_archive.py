from datetime import datetime, timedelta

from currency import model_choices as mch
from currency.models import Rate, Source
from currency.utils import round_decimal

from django.core.management.base import BaseCommand
from django.utils import timezone

import requests


class Command(BaseCommand):
    help = 'Parse Privatbank archive rates'  # noqa

    def handle(self, *args, **options):
        archive_url = 'https://api.privatbank.ua/p24api/exchange_rates'

        end_date = datetime.now(tz=timezone.utc)
        start_date = datetime.now(tz=timezone.utc) - timedelta(
            days=365 * 4)
        total_days = (end_date - start_date).days

        currency_type_mapper = {
            'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
            'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
            'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
            'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC,
        }

        source_name = 'Privatbank'
        bank_url = 'https://privatbank.ua/ '

        source = Source.objects.get_or_create(name=source_name, defaults={'url': bank_url})[0]

        for day in range(total_days):
            current_day = start_date + timedelta(days=day)
            params = {
                'json': '',
                'date': current_day.strftime("%d.%m.%Y"),
            }

            response = requests.get(archive_url, params=params)
            response.raise_for_status()
            rates = response.json()

            for rate in rates["exchangeRate"]:
                if len(rate) < 6:
                    continue
                if 'currency' not in rate or rate['currency'] not in currency_type_mapper:
                    continue
                currency_type = currency_type_mapper.get(rate['currency'])

                if not currency_type:
                    continue

                base_currency_type = currency_type_mapper.get(rate['baseCurrency'])

                sale = round_decimal(rate['saleRate'])
                buy = round_decimal(rate['purchaseRate'])

                try:
                    Rate.objects.get(
                        currency_type=currency_type,
                        base_currency_type=base_currency_type,
                        sale=sale,
                        buy=buy,
                        source=source,
                        created__date=current_day
                    )
                except Rate.DoesNotExist:
                    Rate.objects.create(
                        currency_type=currency_type,
                        base_currency_type=base_currency_type,
                        sale=sale,
                        buy=buy,
                        source=source,
                        created=current_day
                    )
