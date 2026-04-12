# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import date, timedelta


def monday_of_current_week(today=None):
    if today is None:
        today = date.today()
    return today - timedelta(days=today.weekday())


def week_from_offset(offset):
    start = monday_of_current_week() + timedelta(days=offset * 7)
    end = start + timedelta(days=6)
    iso_year, iso_week, _ = start.isocalendar()
    return start, end, iso_year, iso_week


def to_date_key(dt):
    return dt.strftime("%Y-%m-%d")


def format_date_de(dt):
    return dt.strftime("%d.%m.%Y")
