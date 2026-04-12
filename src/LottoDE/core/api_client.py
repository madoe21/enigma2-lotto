# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json

try:
    from urllib import quote_plus
except Exception:
    from urllib.parse import quote_plus

try:
    from urllib2 import Request, urlopen
except Exception:
    from urllib.request import Request, urlopen


class LottoBrandenburgApiClient(object):
    BASE_URL = "https://www.lotto-brandenburg.de"
    FALLBACK_BASE_URL = "http://www.lotto-brandenburg.de"
    DEFAULT_HEADERS = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    }

    def __init__(self):
        self.last_error = ""

    def _fetch_json(self, path):
        self.last_error = ""
        payload = None
        for base_url in (self.BASE_URL, self.FALLBACK_BASE_URL):
            url = "%s%s" % (base_url, path)
            try:
                request = Request(url, headers=self.DEFAULT_HEADERS)
                response = urlopen(request, timeout=15)
                payload = response.read()
                if payload:
                    break
            except Exception as exc:
                self.last_error = str(exc)
                payload = None
                continue

        if not payload:
            return None

        try:
            text = payload.decode("utf-8")
        except Exception:
            text = payload

        try:
            return json.loads(text)
        except Exception:
            self.last_error = "invalid-json"
            return None

    def get_draw_years(self, game_type):
        data = self._fetch_json("/app/getDrawResultYears?gameType=%s" % quote_plus(game_type))
        if isinstance(data, list):
            return data
        return []

    def get_draw_dates(self, game_type, year):
        path = "/app/getDrawResultDates?locale=de&gameType=%s&year=%s" % (
            quote_plus(game_type),
            quote_plus(str(year)),
        )
        data = self._fetch_json(path)
        if isinstance(data, dict):
            return data
        return {}

    def get_draw_results(self, game_type, date_key):
        path = "/app/getDrawResults?locale=de&gameType=%s&date=%s" % (
            quote_plus(game_type),
            quote_plus(date_key),
        )
        data = self._fetch_json(path)
        if isinstance(data, list):
            return data
        return []
