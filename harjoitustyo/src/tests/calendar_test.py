import unittest
from datetime import datetime
from calendar import Calendar

class TestCalendar(unittest.TestCase):
    def test_today_returns_the_current_day(self):
        date = str(Calendar.today()).split(" ")
        compared_date = str(datetime.now()).split(" ")
        self.assertEqual(date[0], compared_date[0]) 
