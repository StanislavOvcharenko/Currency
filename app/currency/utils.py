from decimal import Decimal


def round_decimal(value, precision=4):
    return round(Decimal(value), precision)
