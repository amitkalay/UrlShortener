from flask import *
from flask_restful import Resource
from model.ShortUrlAccess import ShortUrlAccess
from datetime import datetime
from datetime import timedelta
# use timedelta to grab all the stats for a short url here !!


class TinyUrlStats(Resource):
    def get(self):
        input_short_url = request.args.get('short_url')
        hits_since_yesterday = self.get_last_24_hours_accesses(input_short_url)
        return {'last_24_hour_accesses': hits_since_yesterday}

    def get_last_24_hours_accesses(self, input_short_url) -> int:
        now_date = datetime.now()
        yesterday = now_date - timedelta(days=1)
        url_hits = ShortUrlAccess.objects(short_url=input_short_url,
                                          date_accessed__gte=yesterday)

        return len(url_hits)
