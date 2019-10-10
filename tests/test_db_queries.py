import unittest
from mongoengine import *
from model.ShortUrlAccess import ShortUrlAccess
from datetime import datetime
from datetime import timedelta
from resources.TinyUrlStats import TinyUrlStats

# Create a test database in mongo
# create a short url access for now, 5 days ago and 4 months ago
# run all the queries and ensure that they return the right values required
# delete all documents in this collection

connect('test_db')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ShortUrlAccess(short_url='a_short_url').save()
        within_the_week = datetime.now() - timedelta(days=3)
        ShortUrlAccess(short_url='a_short_url', date_accessed=within_the_week).save()
        long_time_ago = datetime.now() - timedelta(weeks=12)
        ShortUrlAccess(short_url='a_short_url', date_accessed=long_time_ago).save()
        recent_reads = TinyUrlStats.get_last_24_hours_accesses(TinyUrlStats(), 'a_short_url')
        week_reads = TinyUrlStats.get_past_week_accesses(TinyUrlStats(), 'a_short_url')
        all_time_reads = TinyUrlStats.get_all_time_accesses(TinyUrlStats(), 'a_short_url')
        self.assertEqual(1, recent_reads)
        self.assertEqual(2, week_reads)
        self.assertEqual(3, all_time_reads)
        ShortUrlAccess.objects().delete()
        disconnect_all()


if __name__ == '__main__':
    unittest.main()
