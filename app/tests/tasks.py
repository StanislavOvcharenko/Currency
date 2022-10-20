from unittest.mock import MagicMock
from currency.models import Rate

from currency.tasks import parsing_privat, parsing_monobank, parsing_vkurse


def test_parsing_privat(mocker):
    response_json = [
        {"ccy": "USD", "base_ccy": "UAH", "buy": "411.00000", "sale": "411.50000"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "39.90000", "sale": "40.90000"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "17668.2920", "sale": "19528.1122"},
    ]

    requests_get_mock = mocker.patch('requests.get', # noqa
                                     return_value=MagicMock(json=lambda: response_json),
                                     )
    initial_rate_count = Rate.objects.count()
    parsing_privat()
    assert Rate.objects.count() == initial_rate_count + 3

    parsing_privat()
    assert Rate.objects.count() == initial_rate_count + 3


def test_parsing_monobank(mocker):
    response_json = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1666213810, "rateBuy": 36.65, "rateSell": 37.4406},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1666245610, "rateBuy": 35.85, "rateSell": 37.4406},
        {"currencyCodeA": 978, "currencyCodeB": 840, "date": 1666213810, "rateBuy": 0.973, "rateSell": 0.988},
        {"currencyCodeA": 826, "currencyCodeB": 980, "date": 1666282246, "rateCross": 42.5382},
        {"currencyCodeA": 392, "currencyCodeB": 980, "date": 1666281739, "rateCross": 0.2513},
        {"currencyCodeA": 756, "currencyCodeB": 980, "date": 1666282249, "rateCross": 37.7185},
        {"currencyCodeA": 156, "currencyCodeB": 980, "date": 1666282045, "rateCross": 5.1831},
        {"currencyCodeA": 784, "currencyCodeB": 980, "date": 1666282055, "rateCross": 10.1878},
        {"currencyCodeA": 971, "currencyCodeB": 980, "date": 1663425223, "rateCross": 0.4252},
        {"currencyCodeA": 8, "currencyCodeB": 980, "date": 1666281967, "rateCross": 0.3137},
        {"currencyCodeA": 51, "currencyCodeB": 980, "date": 1666282167, "rateCross": 0.0929},
        {"currencyCodeA": 973, "currencyCodeB": 980, "date": 1666111345, "rateCross": 0.0865},
        {"currencyCodeA": 32, "currencyCodeB": 980, "date": 1666281700, "rateCross": 0.2444},
        {"currencyCodeA": 36, "currencyCodeB": 980, "date": 1666281366, "rateCross": 23.7108},
        {"currencyCodeA": 944, "currencyCodeB": 980, "date": 1666282032, "rateCross": 22.1187},
        {"currencyCodeA": 50, "currencyCodeB": 980, "date": 1666269256, "rateCross": 0.3541},
        {"currencyCodeA": 975, "currencyCodeB": 980, "date": 1666282255, "rateCross": 18.9069},
        {"currencyCodeA": 48, "currencyCodeB": 980, "date": 1666274015, "rateCross": 99.3372},
        {"currencyCodeA": 108, "currencyCodeB": 980, "date": 1538606522, "rateCross": 0.0158},
        {"currencyCodeA": 96, "currencyCodeB": 980, "date": 1665874173, "rateCross": 26.718},
        {"currencyCodeA": 68, "currencyCodeB": 980, "date": 1666267851, "rateCross": 5.4561},
        {"currencyCodeA": 986, "currencyCodeB": 980, "date": 1666281454, "rateCross": 7.1538},
        {"currencyCodeA": 72, "currencyCodeB": 980, "date": 1663627562, "rateCross": 2.8503},
        {"currencyCodeA": 933, "currencyCodeB": 980, "date": 1666277043, "rateCross": 14.9312},
        {"currencyCodeA": 124, "currencyCodeB": 980, "date": 1666282203, "rateCross": 27.2909},
        {"currencyCodeA": 976, "currencyCodeB": 980, "date": 1655462332, "rateCross": 0.0163},
        {"currencyCodeA": 152, "currencyCodeB": 980, "date": 1666282006, "rateCross": 0.0384},
        {"currencyCodeA": 170, "currencyCodeB": 980, "date": 1666277329, "rateCross": 0.0079},
        {"currencyCodeA": 188, "currencyCodeB": 980, "date": 1666277752, "rateCross": 0.0608},
        {"currencyCodeA": 192, "currencyCodeB": 980, "date": 1666213207, "rateCross": 1.5237},
        {"currencyCodeA": 203, "currencyCodeB": 980, "date": 1666282249, "rateCross": 1.5061},
        {"currencyCodeA": 262, "currencyCodeB": 980, "date": 1666184052, "rateCross": 0.2109},
        {"currencyCodeA": 208, "currencyCodeB": 980, "date": 1666282204, "rateCross": 4.9665},
        {"currencyCodeA": 12, "currencyCodeB": 980, "date": 1666247335, "rateCross": 0.2666},
        {"currencyCodeA": 818, "currencyCodeB": 980, "date": 1666282248, "rateCross": 1.9094},
        {"currencyCodeA": 230, "currencyCodeB": 980, "date": 1666154019, "rateCross": 0.718},
        {"currencyCodeA": 981, "currencyCodeB": 980, "date": 1666282252, "rateCross": 13.69},
        {"currencyCodeA": 936, "currencyCodeB": 980, "date": 1666281892, "rateCross": 2.986},
        {"currencyCodeA": 270, "currencyCodeB": 980, "date": 1666110764, "rateCross": 0.665},
        {"currencyCodeA": 324, "currencyCodeB": 980, "date": 1664815293, "rateCross": 0.0044},
        {"currencyCodeA": 344, "currencyCodeB": 980, "date": 1666265245, "rateCross": 4.7709},
        {"currencyCodeA": 191, "currencyCodeB": 980, "date": 1666282203, "rateCross": 4.9101},
        {"currencyCodeA": 348, "currencyCodeB": 980, "date": 1666282246, "rateCross": 0.0897},
        {"currencyCodeA": 360, "currencyCodeB": 980, "date": 1666282253, "rateCross": 0.0024},
        {"currencyCodeA": 376, "currencyCodeB": 980, "date": 1666282253, "rateCross": 10.6398},
        {"currencyCodeA": 356, "currencyCodeB": 980, "date": 1666281113, "rateCross": 0.455},
        {"currencyCodeA": 368, "currencyCodeB": 980, "date": 1666279580, "rateCross": 0.0256},
        {"currencyCodeA": 364, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0009},
        {"currencyCodeA": 352, "currencyCodeB": 980, "date": 1666281767, "rateCross": 0.2601},
        {"currencyCodeA": 400, "currencyCodeB": 980, "date": 1666279028, "rateCross": 52.8457},
        {"currencyCodeA": 404, "currencyCodeB": 980, "date": 1666270199, "rateCross": 0.3091},
        {"currencyCodeA": 417, "currencyCodeB": 980, "date": 1666278059, "rateCross": 0.4549},
        {"currencyCodeA": 116, "currencyCodeB": 980, "date": 1666005465, "rateCross": 0.0092},
        {"currencyCodeA": 408, "currencyCodeB": 980, "date": 1666213207, "rateCross": 16.6221},
        {"currencyCodeA": 410, "currencyCodeB": 980, "date": 1666280520, "rateCross": 0.0264},
        {"currencyCodeA": 414, "currencyCodeB": 980, "date": 1666192896, "rateCross": 120.8723},
        {"currencyCodeA": 398, "currencyCodeB": 980, "date": 1666282094, "rateCross": 0.0796},
        {"currencyCodeA": 418, "currencyCodeB": 980, "date": 1664596798, "rateCross": 0.0022},
        {"currencyCodeA": 422, "currencyCodeB": 980, "date": 1665833956, "rateCross": 0.0012},
        {"currencyCodeA": 144, "currencyCodeB": 980, "date": 1666282205, "rateCross": 0.1021},
        {"currencyCodeA": 434, "currencyCodeB": 980, "date": 1648958626, "rateCross": 6.4735},
        {"currencyCodeA": 504, "currencyCodeB": 980, "date": 1666280689, "rateCross": 3.3951},
        {"currencyCodeA": 498, "currencyCodeB": 980, "date": 1666282192, "rateCross": 1.9375},
        {"currencyCodeA": 969, "currencyCodeB": 980, "date": 1663928324, "rateCross": 0.0089},
        {"currencyCodeA": 807, "currencyCodeB": 980, "date": 1666281555, "rateCross": 0.5954},
        {"currencyCodeA": 496, "currencyCodeB": 980, "date": 1665918523, "rateCross": 0.0112},
        {"currencyCodeA": 478, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0968},
        {"currencyCodeA": 480, "currencyCodeB": 980, "date": 1666279619, "rateCross": 0.8505},
        {"currencyCodeA": 454, "currencyCodeB": 980, "date": 1633949773, "rateCross": 0.0325},
        {"currencyCodeA": 484, "currencyCodeB": 980, "date": 1666282166, "rateCross": 1.8701},
        {"currencyCodeA": 458, "currencyCodeB": 980, "date": 1666281772, "rateCross": 7.9502},
        {"currencyCodeA": 943, "currencyCodeB": 980, "date": 1665915155, "rateCross": 0.5998},
        {"currencyCodeA": 516, "currencyCodeB": 980, "date": 1665342751, "rateCross": 2.1176},
        {"currencyCodeA": 566, "currencyCodeB": 980, "date": 1666281042, "rateCross": 0.0849},
        {"currencyCodeA": 558, "currencyCodeB": 980, "date": 1666213376, "rateCross": 1.0375},
        {"currencyCodeA": 578, "currencyCodeB": 980, "date": 1666282117, "rateCross": 3.5914},
        {"currencyCodeA": 524, "currencyCodeB": 980, "date": 1666264099, "rateCross": 0.2844},
        {"currencyCodeA": 554, "currencyCodeB": 980, "date": 1666269444, "rateCross": 21.3771},
        {"currencyCodeA": 512, "currencyCodeB": 980, "date": 1666260526, "rateCross": 97.3473},
        {"currencyCodeA": 604, "currencyCodeB": 980, "date": 1666280342, "rateCross": 9.4496},
        {"currencyCodeA": 608, "currencyCodeB": 980, "date": 1666282062, "rateCross": 0.6377},
        {"currencyCodeA": 586, "currencyCodeB": 980, "date": 1666281955, "rateCross": 0.1696},
        {"currencyCodeA": 985, "currencyCodeB": 980, "date": 1666282253, "rateCross": 7.7154},
        {"currencyCodeA": 600, "currencyCodeB": 980, "date": 1666271619, "rateCross": 0.0052},
        {"currencyCodeA": 634, "currencyCodeB": 980, "date": 1666281668, "rateCross": 10.2958},
        {"currencyCodeA": 946, "currencyCodeB": 980, "date": 1666282249, "rateCross": 7.4929},
        {"currencyCodeA": 941, "currencyCodeB": 980, "date": 1666281801, "rateCross": 0.3123},
        {"currencyCodeA": 682, "currencyCodeB": 980, "date": 1666281275, "rateCross": 9.9638},
        {"currencyCodeA": 690, "currencyCodeB": 980, "date": 1666264270, "rateCross": 2.63},
        {"currencyCodeA": 938, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0634},
        {"currencyCodeA": 752, "currencyCodeB": 980, "date": 1666282242, "rateCross": 3.3874},
        {"currencyCodeA": 702, "currencyCodeB": 980, "date": 1666280314, "rateCross": 26.4084},
        {"currencyCodeA": 694, "currencyCodeB": 980, "date": 1664217991, "rateCross": 0.0024},
        {"currencyCodeA": 706, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0647},
        {"currencyCodeA": 968, "currencyCodeB": 980, "date": 1659795594, "rateCross": 1.5023},
        {"currencyCodeA": 760, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0121},
        {"currencyCodeA": 748, "currencyCodeB": 980, "date": 1661589219, "rateCross": 2.2455},
        {"currencyCodeA": 764, "currencyCodeB": 980, "date": 1666282059, "rateCross": 0.9869},
        {"currencyCodeA": 972, "currencyCodeB": 980, "date": 1666278796, "rateCross": 3.6646},
        {"currencyCodeA": 795, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0021},
        {"currencyCodeA": 788, "currencyCodeB": 980, "date": 1666271912, "rateCross": 11.5727},
        {"currencyCodeA": 949, "currencyCodeB": 980, "date": 1666282245, "rateCross": 2.0203},
        {"currencyCodeA": 901, "currencyCodeB": 980, "date": 1666273612, "rateCross": 1.1665},
        {"currencyCodeA": 834, "currencyCodeB": 980, "date": 1666268126, "rateCross": 0.016},
        {"currencyCodeA": 800, "currencyCodeB": 980, "date": 1666252369, "rateCross": 0.0098},
        {"currencyCodeA": 858, "currencyCodeB": 980, "date": 1666277525, "rateCross": 0.9078},
        {"currencyCodeA": 860, "currencyCodeB": 980, "date": 1666282036, "rateCross": 0.0033},
        {"currencyCodeA": 937, "currencyCodeB": 980, "date": 1666213207, "rateCross": 4.3789},
        {"currencyCodeA": 704, "currencyCodeB": 980, "date": 1666272183, "rateCross": 0.0015},
        {"currencyCodeA": 950, "currencyCodeB": 980, "date": 1666267466, "rateCross": 0.056},
        {"currencyCodeA": 952, "currencyCodeB": 980, "date": 1666271861, "rateCross": 0.0563},
        {"currencyCodeA": 886, "currencyCodeB": 980, "date": 1543715495, "rateCross": 0.112},
        {"currencyCodeA": 710, "currencyCodeB": 980, "date": 1666281921, "rateCross": 2.074},
        {"currencyCodeA": 894, "currencyCodeB": 980, "date": 1666213207, "rateCross": 0.0023}]

    requests_get_mock = mocker.patch('requests.get', # noqa
                                     return_value=MagicMock(json=lambda: response_json),
                                     )
    initial_rate_count = Rate.objects.count()
    parsing_monobank()
    assert Rate.objects.count() == initial_rate_count + 3

    parsing_monobank()
    assert Rate.objects.count() == initial_rate_count + 3


def test_parsing_vkurse(mocker):
    response_json = {
        "Dollar": {
            "buy": "40.60",
            "sale": "40.90"
        },
        "Euro": {
            "buy": "39.00",
            "sale": "39.30"
        },
        "Pln": {
            "buy": "7.70",
            "sale": "8.20"
        }
    }
    requests_get_mock = mocker.patch('requests.get', # noqa
                                     return_value=MagicMock(json=lambda: response_json),
                                     )
    initial_rate_count = Rate.objects.count()
    parsing_vkurse()
    assert Rate.objects.count() == initial_rate_count + 2

    parsing_vkurse()
    assert Rate.objects.count() == initial_rate_count + 2
