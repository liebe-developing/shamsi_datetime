import unittest
from shamsi_datetime import ShamsiDateTime
import numpy as np

class TestShamsiDateTime(unittest.TestCase):
    def test_conversion_to_gregorian(self):
        shamsi_date = ShamsiDateTime(1403, 5, 6)
        gregorian_date = shamsi_date.to_gregorian()
        self.assertEqual(str(gregorian_date), '2024-07-27')

    def test_conversion_from_gregorian(self):
        gregorian_date = np.datetime64('2024-07-27')
        shamsi_date = ShamsiDateTime.from_gregorian(gregorian_date)
        self.assertEqual(str(shamsi_date), '1403-05-06')

    def test_equality(self):
        date1 = ShamsiDateTime(1403, 5, 6)
        date2 = ShamsiDateTime(1403, 5, 6)
        self.assertEqual(date1, date2)

if __name__ == '__main__':
    unittest.main()
