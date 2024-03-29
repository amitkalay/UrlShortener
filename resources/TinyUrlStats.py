from flask import *
from flask_restful import Resource
from model.ShortUrlAccess import ShortUrlAccess
from datetime import datetime
from datetime import timedelta


# use timedelta to grab all the stats for a short url here !!


class TinyUrlStats(Resource):
    def get(self):
        input_short_url = request.args.get('short_url')
        if input_short_url is None:
            return {'error': 'please add a short url query parameter like ?short_url=SOME_VALUE '}, 500
        hits_since_yesterday = self.get_last_24_hours_accesses(input_short_url)
        hits_since_last_week = self.get_past_week_accesses(input_short_url)
        all_time_hits = self.get_all_time_accesses(input_short_url)
        return {
            'short_url_accessed': input_short_url,
            'last_24_hour_accesses': hits_since_yesterday,
            'last_week_accesses': hits_since_last_week,
            'all_time_hits': all_time_hits
        }

    def get_last_24_hours_accesses(self, input_short_url) -> int:
        now_date = datetime.now()
        yesterday = now_date - timedelta(days=1)
        url_hits = ShortUrlAccess.objects(short_url=input_short_url,
                                          date_accessed__gte=yesterday)

        return len(url_hits)

    def get_past_week_accesses(self, input_short_url) -> int:
        now_date = datetime.now()
        last_week = now_date - timedelta(weeks=1)
        url_hits = ShortUrlAccess.objects(short_url=input_short_url,
                                          date_accessed__gte=last_week)

        return len(url_hits)

    def get_all_time_accesses(self, input_short_url) -> int:
        url_hits = ShortUrlAccess.objects(short_url=input_short_url)
        return len(url_hits)
