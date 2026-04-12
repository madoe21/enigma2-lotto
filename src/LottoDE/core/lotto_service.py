# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import date, timedelta

from .models import DrawDisplay, WeekGameData, WeekViewData
from .week_logic import format_date_de, to_date_key, week_from_offset


class LottoWeekService(object):
    GAME_CONFIG = [
        {
            "title": "Eurojackpot",
            "api_game_type": "EURO",
            "weekday_offsets": [1, 4],  # Tuesday, Friday
            "main_count": 5,
            "special_count": 2,
            "special_label": "Eurozahlen",
        },
        {
            "title": "LOTTO 6aus49",
            "api_game_type": "LOTTO",
            "weekday_offsets": [2, 5],  # Wednesday, Saturday
            "main_count": 6,
            "special_count": 1,
            "special_label": "Superzahl",
        },
    ]

    def __init__(self, api_client):
        self.api = api_client
        self._draw_dates_cache = {}
        self._draw_results_cache = {}

    def build_week(self, offset):
        week_start, week_end, iso_year, iso_week = week_from_offset(offset)
        games = []
        problem_count = 0
        checked_count = 0
        today = date.today()
        for game in self.GAME_CONFIG:
            game_data, checked, problems = self._build_game_rows(game, week_start, offset, today)
            games.append(game_data)
            checked_count += checked
            problem_count += problems

        status_hint = ""
        if checked_count > 0 and problem_count > 0:
            status_hint = "Hinweis: %d Ziehungen ohne Zahlen (API/Netz)" % problem_count
            api_error = getattr(self.api, "last_error", "")
            if api_error:
                status_hint = "%s [%s]" % (status_hint, api_error)

        return WeekViewData(week_start, week_end, iso_year, iso_week, games, status_hint)

    def _cache_key(self, game_type, year):
        return "%s:%s" % (game_type, str(year))

    def _get_draw_dates_for_year(self, game_type, year):
        key = self._cache_key(game_type, year)
        cached = self._draw_dates_cache.get(key)
        if cached is not None:
            return cached

        dates = self.api.get_draw_dates(game_type, year)
        self._draw_dates_cache[key] = dates
        return dates

    def _get_result_for_date(self, game_type, date_key):
        cache_key = "%s:%s" % (game_type, date_key)
        cached = self._draw_results_cache.get(cache_key)
        if cached is not None:
            return cached

        rows = self.api.get_draw_results(game_type, date_key)
        selected = None
        for row in rows:
            if isinstance(row, dict) and row.get("gameType") == game_type:
                selected = row
                break

        self._draw_results_cache[cache_key] = selected
        return selected

    def _build_game_rows(self, game_cfg, week_start, offset, today):
        game_type = game_cfg["api_game_type"]
        draws = []
        checked_count = 0
        problem_count = 0

        for day_offset in game_cfg["weekday_offsets"]:
            draw_date = week_start + timedelta(days=day_offset)

            # In current week, hide draws that have not happened yet.
            if offset == 0 and draw_date > today:
                draws.append(
                    DrawDisplay(
                        date_key=to_date_key(draw_date),
                        date_label="",
                        main_numbers=[],
                        special_numbers=[],
                        special_label=game_cfg["special_label"],
                        is_available=False,
                        issue="future-hidden",
                    )
                )
                continue

            checked_count += 1
            date_key = to_date_key(draw_date)

            draw_dates = self._get_draw_dates_for_year(game_type, draw_date.year)
            date_label = draw_dates.get(date_key)

            if not date_label:
                date_label = "%s (keine Ziehung)" % format_date_de(draw_date)
                draws.append(
                    DrawDisplay(
                        date_key=date_key,
                        date_label=date_label,
                        main_numbers=[],
                        special_numbers=[],
                        special_label=game_cfg["special_label"],
                        is_available=False,
                        issue="no-draw",
                    )
                )
                continue

            result = self._get_result_for_date(game_type, date_key)
            if not result:
                problem_count += 1
                draws.append(
                    DrawDisplay(
                        date_key=date_key,
                        date_label=date_label,
                        main_numbers=[],
                        special_numbers=[],
                        special_label=game_cfg["special_label"],
                        is_available=False,
                        issue="no-result",
                    )
                )
                continue

            main_numbers = self._normalize_number_list(result.get("sortedWinningDigits") or result.get("winningDigits"), game_cfg["main_count"])
            special_numbers = self._extract_special_numbers(result, game_type, game_cfg["special_count"])

            draws.append(
                DrawDisplay(
                    date_key=date_key,
                    date_label=date_label,
                    main_numbers=main_numbers,
                    special_numbers=special_numbers,
                    special_label=game_cfg["special_label"],
                    is_available=bool(main_numbers),
                    issue="" if main_numbers else "empty-numbers",
                )
            )
            if not main_numbers:
                problem_count += 1

        return WeekGameData(game_cfg["title"], draws), checked_count, problem_count

    def _extract_special_numbers(self, result, game_type, count):
        if game_type == "EURO":
            return self._normalize_number_list(result.get("sortedSecondaryWinningDigits") or result.get("secondaryWinningDigits"), count)

        if game_type == "LOTTO":
            super_number = result.get("superNumber")
            if super_number is None or super_number == "":
                return []
            return [str(super_number)]

        return []

    def _normalize_number_list(self, values, max_count):
        if not isinstance(values, list):
            return []

        normalized = []
        for item in values:
            if item is None:
                continue
            txt = str(item).strip()
            if not txt:
                continue
            normalized.append(txt)
            if len(normalized) >= max_count:
                break
        return normalized
