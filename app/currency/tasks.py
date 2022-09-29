import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from currency import model_choices as mch

from currency.utils import round_decimal
from currency.models import Rate, Source


@shared_task
def send_contactus_mail(email_to, message):
    subject = 'Contact us Currency'
    message = f'''subject from client {subject}
    Email: {email_to}
        Message : {message}
        '''

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )


@shared_task
def parsing_privat():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()

    currency_type_mapper = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
        'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC
    }

    source_name = 'Privatbank'
    bank_url = 'https://privatbank.ua/ '

    source = Source.objects.get_or_create(name=source_name, defaults={'url': bank_url})[0]

    for rate in response_data:
        base_currency_type = rate['base_ccy']
        currency_type = rate['ccy']

        if currency_type not in currency_type_mapper or base_currency_type not in currency_type_mapper:
            continue

        base_currency_type = currency_type_mapper[rate['base_ccy']]
        currency_type = currency_type_mapper[rate['ccy']]
        sale = round_decimal(rate['sale'])
        buy = round_decimal(rate['buy'])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or latest_rate.sale != sale or latest_rate.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source
            )


@shared_task
def parsing_monobank():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    response_data_mono = response.json()

    currency_type_mapper = {
        '980': mch.CurrencyType.CURRENCY_TYPE_UAH,
        '840': mch.CurrencyType.CURRENCY_TYPE_USD,
        '978': mch.CurrencyType.CURRENCY_TYPE_EUR,
        # 'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC
    }

    source_name = 'Monobank'
    bank_url = 'https://www.monobank.ua/'

    source = Source.objects.get_or_create(name=source_name, defaults={'url': bank_url})[0]

    for rate_mono in response_data_mono:
        base_currency_type = str(rate_mono['currencyCodeA'])
        currency_type = str(rate_mono['currencyCodeB'])

        if currency_type not in currency_type_mapper or base_currency_type not in currency_type_mapper:
            continue

        base_currency_type = currency_type_mapper[str(rate_mono['currencyCodeA'])]
        currency_type = currency_type_mapper[str(rate_mono['currencyCodeB'])]
        sale = round_decimal(rate_mono['rateSell'])
        buy = round_decimal(rate_mono['rateBuy'])

        try:
            latest_rate_mono = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate_mono = None

        if latest_rate_mono is None or latest_rate_mono.sale != sale or latest_rate_mono.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source
            )


@shared_task
def parsing_vkurse():
    url = 'https://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    response_data_vkurse = response.json()

    currency_type_mapper = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'Dollar': mch.CurrencyType.CURRENCY_TYPE_USD,
        'Euro': mch.CurrencyType.CURRENCY_TYPE_EUR,
        # 'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC
    }

    source_name = 'Vkurse'
    bank_url = 'https://www.vkurse.dp.ua/'

    source, create = Source.objects.get_or_create(name=source_name, defaults={'source_url': bank_url})

    for rate_vkurse in response_data_vkurse:
        base_currency_type = 'UAH'
        currency_type = str(rate_vkurse)

        if currency_type not in currency_type_mapper or base_currency_type not in currency_type_mapper:
            continue

        base_currency_type = currency_type_mapper['UAH']
        currency_type = currency_type_mapper[rate_vkurse]
        sale = round_decimal(response_data_vkurse[rate_vkurse]['sale'])
        buy = round_decimal(response_data_vkurse[rate_vkurse]['buy'])

        try:
            latest_rate_mono = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate_mono = None

        if latest_rate_mono is None or latest_rate_mono.sale != sale or latest_rate_mono.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source
            )


@shared_task
def parsing_nacbank():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    response.raise_for_status()
    response_data_nacbank = response.json()

    currency_type_mapper = {

        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH
    }

    source_name = 'Nacbank'
    bank_url = 'https://bank.gov.ua/'

    source, create = Source.objects.get_or_create(name=source_name, defaults={'source_url': bank_url})

    for rate_nacbank in response_data_nacbank:
        base_currency_type = rate_nacbank['cc']
        currency_type = 'UAH'

        if currency_type not in currency_type_mapper or base_currency_type not in currency_type_mapper:
            continue

        base_currency_type = currency_type_mapper[rate_nacbank['cc']]
        currency_type = 'UAH'
        sale = round_decimal(rate_nacbank['rate'])
        buy = None

        try:
            latest_rate_nacbank = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate_nacbank = None

        if latest_rate_nacbank is None or latest_rate_nacbank.sale != sale or latest_rate_nacbank.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source
            )


@shared_task
def parsing_apilayer():
    header_api = {'apikey': '4vzCc1MZQnjgqJxATPWTZrvKxT3suTDR'}
    url = 'https://api.apilayer.com/currency_data/live?base=UAH&symbols=EUR,USD'
    response = requests.get(url, headers=header_api)
    response.raise_for_status()
    response_data_apilayer = response.json()

    currency_type_mapper = {
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH
    }

    source_name = 'Apilayer'
    bank_url = 'https://apilayer.com/marketplace/currency_data-api'

    source, create = Source.objects.get_or_create(name=source_name, defaults={'source_url': bank_url})

    base_currency_type = 'UAH'
    currency_type = currency_type_mapper[response_data_apilayer['source']]
    sale = round_decimal(response_data_apilayer['quotes']['USDUAH'])
    buy = None

    try:
        latest_rate_apilayer = Rate.objects.filter(
            base_currency_type=base_currency_type,
            currency_type=currency_type,
            source=source
        ).latest('created')
    except Rate.DoesNotExist:
        latest_rate_apilayer = None

    if latest_rate_apilayer is None or latest_rate_apilayer.sale != sale or latest_rate_apilayer.buy != buy:
        Rate.objects.create(
            base_currency_type=base_currency_type,
            currency_type=currency_type,
            sale=sale,
            buy=buy,
            source=source
        )
