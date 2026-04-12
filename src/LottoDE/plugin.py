# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from Plugins.Plugin import PluginDescriptor
from Tools.Directories import SCOPE_PLUGINS, resolveFilename

from . import _
from .core.api_client import LottoBrandenburgApiClient
from .core.lotto_service import LottoWeekService
from .screens import LottoMainScreen

_APP = None

# True: use aspect-specific transparent icon files (no cropping, no clipping).
# False: always use the original plugin.png (can look larger but may be stretched by skin).
USE_ASPECT_ICON_VARIANTS = True


class AppContext(object):
    def __init__(self):
        self.api = LottoBrandenburgApiClient()
        self.week_service = LottoWeekService(self.api)

    def get_week_view(self, offset):
        return self.week_service.build_week(offset)

    def clear_result_cache(self):
        self.week_service._draw_results_cache = {}


class LottoFacade(object):
    def __init__(self, app_context):
        self._ctx = app_context

    def get_week_view(self, offset):
        return self._ctx.get_week_view(offset)

    def clear_result_cache(self):
        self._ctx.clear_result_cache()


class ScreenAppAdapter(object):
    def __init__(self, app_context):
        self.service = LottoFacade(app_context)


def get_app():
    global _APP
    if _APP is None:
        _APP = AppContext()
    return _APP


def main(session, **kwargs):
    app = ScreenAppAdapter(get_app())
    session.open(LottoMainScreen, app)


def _icon_file_for_aspect_ratio():
    try:
        from enigma import getDesktop

        size = getDesktop(0).size()
        width = int(size.width())
        height = int(size.height())
        if height > 0:
            ratio = float(width) / float(height)
            if ratio < 1.2:
                return "plugin_1x1.png"
            if ratio < 1.5:
                return "plugin_4x3.png"
            if ratio < 1.7:
                return "plugin_16x10.png"
            return "plugin_16x9.png"
    except Exception:
        pass

    return "plugin_16x9.png"


def _resolve_plugin_icon_path():
    if not USE_ASPECT_ICON_VARIANTS:
        return resolveFilename(SCOPE_PLUGINS, "Extensions/LottoDE/res/plugin.png")

    icon_name = _icon_file_for_aspect_ratio()
    icon_path = resolveFilename(SCOPE_PLUGINS, "Extensions/LottoDE/res/%s" % icon_name)
    if os.path.exists(icon_path):
        return icon_path
    return resolveFilename(SCOPE_PLUGINS, "Extensions/LottoDE/res/plugin.png")


def Plugins(**kwargs):
    plugin_icon = _resolve_plugin_icon_path()
    return [
        PluginDescriptor(
            name="Lotto DE",
            description=_("Lottozahlen"),
            where=PluginDescriptor.WHERE_PLUGINMENU,
            icon=plugin_icon,
            fnc=main,
        )
    ]
