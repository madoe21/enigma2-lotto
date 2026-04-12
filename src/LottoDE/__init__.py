# -*- coding: utf-8 -*-
from __future__ import absolute_import

import gettext

from Components.Language import language
from Tools.Directories import SCOPE_PLUGINS, resolveFilename

PLUGIN_DOMAIN = "LottoDE"
PLUGIN_PATH = "Extensions/LottoDE/locale"

_DE_FALLBACK = {
    "Lottozahlen": "Lottozahlen",
    "Current week": "Aktuelle Woche",
    "Previous week": "Vorherige Woche",
    "Next week": "Nächste Woche",
    "Refresh": "Aktualisieren",
    "Back": "Zurück",
    "Info": "Info",
    "No data": "Keine Daten",
    "Could not load draw data": "Ziehungsdaten konnten nicht geladen werden",
    "Week": "Woche",
    "Eurojackpot": "Eurojackpot",
    "LOTTO 6aus49": "LOTTO 6aus49",
    "Support": "Support",
}


def localeInit():
    gettext.bindtextdomain(PLUGIN_DOMAIN, resolveFilename(SCOPE_PLUGINS, PLUGIN_PATH))


def _(txt):
    translated = gettext.dgettext(PLUGIN_DOMAIN, txt)
    if translated != txt:
        return translated

    try:
        lang = language.getLanguage()[:2]
    except Exception:
        lang = "en"

    if lang == "de":
        return _DE_FALLBACK.get(txt, txt)
    return txt


localeInit()
try:
    language.addCallback(localeInit)
except Exception:
    pass
