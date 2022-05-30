from datetime import date
from unittest import TestCase

from stock.stock_exchange_holidays import Holidays, NYSE, CME, B3


class TestNYSE(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=NYSE())
        self.nyse_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            date(2020, 1, 1): True,
            date(2020, 1, 20): True,
            date(2020, 2, 17): True,
            date(2020, 4, 10): True,
            date(2020, 5, 25): True,
            date(2020, 7, 4): True,
            date(2020, 9, 7): True,
            date(2020, 11, 26): True,
            date(2020, 12, 25): True,
            date(2020, 12, 26): False,
            date(2021, 1, 1): True,
            date(2021, 1, 18): True,
            date(2021, 2, 15): True,
            date(2021, 4, 2): True,
            date(2021, 5, 31): True,
            date(2021, 7, 4): True,
            date(2021, 9, 6): True,
            date(2021, 11, 25): True,
            date(2021, 12, 25): True,
            date(2021, 12, 26): False,
            date(2022, 1, 1): True,
            date(2022, 1, 17): True,
            date(2022, 2, 21): True,
            date(2022, 4, 15): True,
            date(2022, 5, 30): True,
            date(2022, 7, 4): True,
            date(2022, 9, 5): True,
            date(2022, 11, 24): True,
            date(2022, 12, 25): True,
            date(2022, 12, 26): False,
            date(2023, 1, 1): True,
            date(2023, 1, 16): True,
            date(2023, 2, 20): True,
            date(2023, 4, 7): True,
            date(2023, 5, 29): True,
            date(2023, 7, 4): True,
            date(2023, 9, 4): True,
            date(2023, 11, 23): True,
            date(2023, 12, 25): True,
            date(2023, 12, 26): False,
        }

    def test_nyse_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

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
        self.assertEqual(len(holidays_by_year), 10)

    def test_nyse_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 10)

    def test_nyse_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_nyse_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)


class TestCME(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=CME())
        self.cme_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            date(2020, 1, 1): True,
            date(2020, 1, 20): True,
            date(2020, 2, 17): True,
            date(2020, 4, 10): True,
            date(2020, 5, 25): True,
            date(2020, 7, 4): True,
            date(2020, 9, 7): True,
            date(2020, 11, 26): True,
            date(2020, 12, 25): True,
            date(2020, 12, 26): False,
            date(2021, 1, 1): True,
            date(2021, 1, 18): True,
            date(2021, 2, 15): True,
            date(2021, 4, 2): True,
            date(2021, 5, 31): True,
            date(2021, 7, 4): True,
            date(2021, 9, 6): True,
            date(2021, 11, 25): True,
            date(2021, 12, 25): True,
            date(2021, 12, 26): False,
            date(2022, 1, 1): True,
            date(2022, 1, 17): True,
            date(2022, 2, 21): True,
            date(2022, 4, 15): True,
            date(2022, 5, 30): True,
            date(2022, 7, 4): True,
            date(2022, 9, 5): True,
            date(2022, 11, 24): True,
            date(2022, 12, 25): True,
            date(2022, 12, 26): False,
        }

    def test_cme_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

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
        self.assertEqual(len(holidays_by_year), 10)

    def test_cme_holidays_2021(self):
        year = 2021
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 10)

    def test_cme_holidays_2022(self):
        year = 2022
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)

    def test_cme_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 11)


class TestB3(TestCase):

    def setUp(self):
        self.holidays = Holidays(exchange=B3())
        self.b3_holidays = self.holidays.get_holidays()

        self.all_holidays = {
            date(2020, 1, 1): True,
            date(2020, 2, 24): True,
            date(2020, 2, 25): True,
            date(2020, 4, 10): True,
            date(2020, 4, 21): True,
            date(2020, 5, 1): True,
            date(2020, 6, 11): True,
            date(2020, 7, 9): True,
            date(2020, 9, 7): True,
            date(2020, 10, 12): True,
            date(2020, 11, 2): True,
            date(2020, 11, 15): True,
            date(2020, 12, 25): True,
            date(2020, 12, 26): False,
            date(2020, 12, 31): True,
            date(2021, 1, 1): True,
            date(2021, 1, 25): True,
            date(2021, 2, 15): True,
            date(2021, 2, 16): True,
            date(2021, 4, 2): True,
            date(2021, 4, 21): True,
            date(2021, 5, 1): True,
            date(2021, 6, 3): True,
            date(2021, 7, 9): True,
            date(2021, 9, 7): True,
            date(2021, 10, 12): True,
            date(2021, 11, 2): True,
            date(2021, 11, 15): True,
            date(2021, 12, 25): True,
            date(2021, 12, 31): True,
            date(2021, 12, 26): False,
            date(2022, 1, 1): True,
            date(2022, 2, 28): True,
            date(2022, 3, 1): True,
            date(2022, 4, 15): True,
            date(2022, 4, 21): True,
            date(2022, 5, 1): True,
            date(2022, 6, 16): True,
            date(2022, 9, 7): True,
            date(2022, 10, 12): True,
            date(2022, 11, 2): True,
            date(2022, 11, 15): True,
            date(2022, 12, 25): True,
            date(2022, 12, 31): True,
            date(2022, 12, 26): False,
        }

    def test_b3_all_holidays(self):
        for holiday in self.all_holidays.items():
            if holiday[1]:
                self.assertTrue(self.holidays.is_date_holiday(holiday[0]))
            else:
                self.assertFalse(self.holidays.is_date_holiday(holiday[0]))

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

    def test_b3_holidays_2023(self):
        year = 2023
        holidays_by_year = self.holidays.get_holidays_by_year(year)
        self.assertEqual(len(holidays_by_year), 13)
