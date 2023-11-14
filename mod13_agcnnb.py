import unittest
from datetime import datetime

class TestStock(unittest.TestCase):

    def test_symbol(self):
        symbol = input("Enter a stock symbol: ")
        self.assertEqual(symbol.upper(), symbol)
        self.assertTrue(symbol.isalpha())
        self.assertLessEqual(len(symbol), 7)
        self.assertGreaterEqual(len(symbol), 1)

    def test_chart(self):
        type = input("Enter chart type: ")
        self.assertTrue(type.isnumeric())
        self.assertLessEqual(int(type), 2)
        self.assertGreaterEqual(int(type), 1)

    def test_series(self):
        series = input("Enter time series: ")
        self.assertTrue(series.isnumeric())
        self.assertLessEqual(int(series), 4)
        self.assertGreaterEqual(int(series), 1)

    def test_start_date(self):
        format = "%d-%m-%Y"
        date = input("Enter start date: ")
        self.assertTrue(datetime.strptime(date, format))

    def test_end_date(self):
        format = "%d-%m-%Y"
        date = input("Enter end date: ")
        self.assertTrue(datetime.strptime(date, format))

if __name__ == '__main__':
    unittest.main()
