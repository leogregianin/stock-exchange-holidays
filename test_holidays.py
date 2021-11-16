from datetime import date
from unittest import TestCase

from stock_exchange_holidays import Holidays, NYSE, CME, B3


class TestNYSE(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=NYSE())
        self.nyse_holidays = self.holidays.get_holidays()

    def test_nyse_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_nyse_independence_day_is_holiday(self):
        get_date = date(2022, 7, 4)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_nyse_random_date_is_not_holiday(self):
        get_date = date(2020, 1, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_nyse_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)

    def test_nyse_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)

    def test_nyse_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)

    def test_nyse_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)


class TestCME(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=CME())
        self.cme_holidays = self.holidays.get_holidays()

    def test_cme_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_cme_independence_day_is_holiday(self):
        get_date = date(2022, 7, 4)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_cme_random_date_is_not_holiday(self):
        get_date = date(2020, 1, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_cme_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)

    def test_cme_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)

    def test_cme_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 9)


class TestB3(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=B3())
        self.b3_holidays = self.holidays.get_holidays()

    def test_b3_first_day_year_is_holiday(self):
        get_date = date(2020, 1, 1)
        self.assertTrue(self.holidays.is_date_holiday(get_date))

    def test_b3_random_date_is_not_holiday(self):
        get_date = date(2020, 1, 10)
        self.assertFalse(self.holidays.is_date_holiday(get_date))

    def test_b3_holidays_2020(self):
        year = 2020
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 14)

    def test_b3_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 15)

    def test_b3_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 13)
