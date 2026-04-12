# -*- coding: utf-8 -*-
from __future__ import absolute_import


class DrawDisplay(object):
    def __init__(self, date_key, date_label, main_numbers, special_numbers, special_label, is_available, issue=None):
        self.date_key = date_key
        self.date_label = date_label
        self.main_numbers = main_numbers or []
        self.special_numbers = special_numbers or []
        self.special_label = special_label or ""
        self.is_available = bool(is_available)
        self.issue = issue or ""


class WeekGameData(object):
    def __init__(self, title, draw_rows):
        self.title = title
        self.draw_rows = draw_rows or []


class WeekViewData(object):
    def __init__(self, week_start, week_end, iso_year, iso_week, games, status_hint=""):
        self.week_start = week_start
        self.week_end = week_end
        self.iso_year = iso_year
        self.iso_week = iso_week
        self.games = games or []
        self.status_hint = status_hint or ""
