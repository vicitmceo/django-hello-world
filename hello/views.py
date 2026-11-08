import random

from django.shortcuts import render
from django.utils import timezone

WEEKDAYS = [
    "Понеділок", "Вівторок", "Середа", "Четвер",
    "П'ятниця", "Субота", "Неділя",
]

QUOTES = [
    "Єдиний спосіб робити чудову роботу — любити те, що ти робиш. — Стів Джобс",
    "Знання — сила. — Френсіс Бекон",
    "В своїй хаті своя правда, і сила, і воля. — Тарас Шевченко",
    "Contra spem spero (Без надії сподіваюсь). — Леся Українка",
    "Терпіння і труд все перетруть. — народна мудрість",
    "Тихше їдеш — далі будеш. — народна мудрість",
    "Усе геніальне — просте. — народна мудрість",
]


def weekday_name(moment=None) -> str:
    """Назва дня тижня українською для вказаного (або поточного) часу."""
    moment = moment or timezone.localtime()
    return WEEKDAYS[moment.weekday()]


def home(request):
    context = {"weekday": weekday_name(), "quote": random.choice(QUOTES)}
    return render(request, "hello/home.html", context)
