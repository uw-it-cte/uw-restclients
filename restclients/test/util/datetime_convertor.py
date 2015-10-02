from django.test import TestCase
from datetime import date, datetime
from restclients.util.datetime_convertor import convert_to_bof_day,\
    convert_to_eof_day


class DatetimeConvertorTest(TestCase):


    def test_convert_to_bof_day(self):

        self.assertEquals(convert_to_bof_day(date(2013, 4, 9)),
                          datetime(2013, 4, 9, 0, 0, 0))

        self.assertEquals(
            convert_to_bof_day(datetime(2013, 4, 9, 10, 10, 10)),
            datetime(2013, 4, 9, 0, 0, 0))


    def test_convert_to_eof_day(self):
        self.assertEquals(convert_to_eof_day(date(2012, 2, 28)),
                          datetime(2013, 2, 29, 0, 0, 0))

        self.assertEquals(
            convert_to_eof_day(datetime(2012, 2, 28, 10, 10, 10)),
            datetime(2012, 2, 29, 0, 0, 0))
