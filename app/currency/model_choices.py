from django.db import models

# CURRENCY_TYPE_UAH = 'UAH'
# CURRENCY_TYPE_USD = 'USD'
# CURRENCY_TYPE_EUR = 'EUR'
# CURRENCY_TYPE_BTC = 'BTC'
#
# CURRENCY_TYPES = (
#     (CURRENCY_TYPE_UAH, 'Hryvna'),
#     (CURRENCY_TYPE_USD, 'Dollar'),
#     (CURRENCY_TYPE_BTC, 'Bitcoin'),
#     (CURRENCY_TYPE_EUR, 'Euro')
# )

class CurrencyType(models.TextChoices):
    CURRENCY_TYPE_UAH = 'UAH', 'Hryvna'
    CURRENCY_TYPE_USD = 'USD', 'Dollar'
    CURRENCY_TYPE_EUR = 'EUR', 'Euro'
    CURRENCY_TYPE_BTC = 'BTC', 'Bitcoin'
