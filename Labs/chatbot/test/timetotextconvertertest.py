from unittest import TestCase
from datetime import time


class TimeToTextTest(TestCase):

    converter = None

    def setUp(self):
        self.converter = TimeToTestTestConverter()

    def test_can_do_midnight(self):
        result = self.converter.convert(time(0, 0))
        self.assertEqual('midnight', result)

class TimeToTestTestConverter:

    def convert(self, input_time):
        if input_time.hour == 0 and input_time.minute == 0:
            return 'midnight'
        else:
            return None