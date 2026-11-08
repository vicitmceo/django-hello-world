from datetime import datetime

from django.test import TestCase

from .views import QUOTES, WEEKDAYS, weekday_name


class HomeTest(TestCase):
    def test_home_shows_hello_weekday_and_quote(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello, World!")
        self.assertTrue(any(day in response.content.decode() for day in WEEKDAYS))
        self.assertTrue(any(q.split(" — ")[0] in response.content.decode() for q in QUOTES))

    def test_weekday_name_is_ukrainian(self):
        self.assertEqual(weekday_name(datetime(2026, 11, 9)), "Понеділок")
        self.assertEqual(weekday_name(datetime(2026, 11, 15)), "Неділя")
