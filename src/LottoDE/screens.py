# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from Components.ActionMap import ActionMap
from Components.Pixmap import Pixmap
from Components.Sources.StaticText import StaticText
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Tools.Directories import SCOPE_PLUGINS, resolveFilename

from . import _


class LottoMainScreen(Screen):
    skin = """
        <screen name="LottoMainScreen" position="center,70" size="1200,650" title="Lottozahlen">
            <widget source="title" render="Label" position="30,16" size="760,40" font="Regular;34" />
            <widget source="week" render="Label" position="30,56" size="900,34" font="Regular;28" foregroundColor="#bbbbbb" />
            <widget source="status" render="Label" position="30,92" size="980,30" font="Regular;24" foregroundColor="#aaaaaa" />

            <widget source="e_title" render="Label" position="30,140" size="450,34" font="Regular;30" />
            <widget source="e_row1_date" render="Label" position="30,180" size="340,36" font="Regular;24" />
            <widget source="e_row2_date" render="Label" position="30,232" size="340,36" font="Regular;24" />

            <widget source="l_title" render="Label" position="30,320" size="450,34" font="Regular;30" />
            <widget source="l_row1_date" render="Label" position="30,360" size="340,36" font="Regular;24" />
            <widget source="l_row2_date" render="Label" position="30,412" size="340,36" font="Regular;24" />

            <widget source="hint" render="Label" position="30,470" size="1100,30" font="Regular;22" foregroundColor="#9a9a9a" />
            <widget source="support" render="Label" position="30,504" size="1100,26" font="Regular;20" foregroundColor="#7f7f7f" />

            <ePixmap pixmap="skin_default/buttons/red.png" position="30,560" size="220,30" alphatest="on" />
            <ePixmap pixmap="skin_default/buttons/green.png" position="260,560" size="220,30" alphatest="on" />
            <ePixmap pixmap="skin_default/buttons/yellow.png" position="490,560" size="220,30" alphatest="on" />
            <ePixmap pixmap="skin_default/buttons/blue.png" position="720,560" size="250,30" alphatest="on" />
            <widget source="key_red" render="Label" position="30,560" size="220,30" font="Regular;22" halign="center" valign="center" transparent="1" />
            <widget source="key_green" render="Label" position="260,560" size="220,30" font="Regular;22" halign="center" valign="center" transparent="1" />
            <widget source="key_yellow" render="Label" position="490,560" size="220,30" font="Regular;22" halign="center" valign="center" transparent="1" />
            <widget source="key_blue" render="Label" position="720,560" size="250,30" font="Regular;22" halign="center" valign="center" transparent="1" />

            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="380,180" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="436,180" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="492,180" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="548,180" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="604,180" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="678,180" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="734,180" size="46,46" alphatest="blend" zPosition="1" />

            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="380,232" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="436,232" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="492,232" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="548,232" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="604,232" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="678,232" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="734,232" size="46,46" alphatest="blend" zPosition="1" />

            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="380,360" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="436,360" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="492,360" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="548,360" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="604,360" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="660,360" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="734,360" size="46,46" alphatest="blend" zPosition="1" />

            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="380,412" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="436,412" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="492,412" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="548,412" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="604,412" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="660,412" size="46,46" alphatest="blend" zPosition="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LottoDE/res/ball_white.png" position="734,412" size="46,46" alphatest="blend" zPosition="1" />

            <widget source="e1_1" render="Label" position="380,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e1_2" render="Label" position="436,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e1_3" render="Label" position="492,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e1_4" render="Label" position="548,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e1_5" render="Label" position="604,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e1_6" render="Label" position="678,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e1_7" render="Label" position="734,180" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />

            <widget source="e2_1" render="Label" position="380,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e2_2" render="Label" position="436,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e2_3" render="Label" position="492,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e2_4" render="Label" position="548,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e2_5" render="Label" position="604,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e2_6" render="Label" position="678,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="e2_7" render="Label" position="734,232" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />

            <widget source="l1_1" render="Label" position="380,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l1_2" render="Label" position="436,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l1_3" render="Label" position="492,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l1_4" render="Label" position="548,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l1_5" render="Label" position="604,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l1_6" render="Label" position="660,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l1_7" render="Label" position="734,360" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />

            <widget source="l2_1" render="Label" position="380,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l2_2" render="Label" position="436,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l2_3" render="Label" position="492,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l2_4" render="Label" position="548,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l2_5" render="Label" position="604,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l2_6" render="Label" position="660,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
            <widget source="l2_7" render="Label" position="734,412" size="46,46" font="Regular;25" halign="center" valign="center" foregroundColor="#000000" transparent="1" zPosition="2" />
        </screen>
    """

    BALL_GROUPS = [
        ["e1_1", "e1_2", "e1_3", "e1_4", "e1_5", "e1_6", "e1_7"],
        ["e2_1", "e2_2", "e2_3", "e2_4", "e2_5", "e2_6", "e2_7"],
        ["l1_1", "l1_2", "l1_3", "l1_4", "l1_5", "l1_6", "l1_7"],
        ["l2_1", "l2_2", "l2_3", "l2_4", "l2_5", "l2_6", "l2_7"],
    ]

    def __init__(self, session, app):
        Screen.__init__(self, session)
        self.app = app
        self.week_offset = 0

        self["title"] = StaticText(_("Lottozahlen"))
        self["week"] = StaticText("")
        self["status"] = StaticText("")
        self["e_title"] = StaticText(_("Eurojackpot"))
        self["e_row1_date"] = StaticText("")
        self["e_row2_date"] = StaticText("")
        self["l_title"] = StaticText(_("LOTTO 6aus49"))
        self["l_row1_date"] = StaticText("")
        self["l_row2_date"] = StaticText("")
        self["hint"] = StaticText("Linke/Rechte Pfeiltaste: Woche wechseln")
        self["support"] = StaticText("Support: buymeacoffee.com/madoe21")

        self["key_red"] = StaticText(_("Close"))
        self["key_green"] = StaticText(_("Refresh"))
        self["key_yellow"] = StaticText(_("Current week"))
        self["key_blue"] = StaticText(_("Information"))

        for group in self.BALL_GROUPS:
            for name in group:
                self[name] = StaticText("")

        self["actions"] = ActionMap(
            ["ColorActions", "OkCancelActions", "DirectionActions"],
            {
                "cancel": self.close,
                "red": self.close,
                "green": self.key_refresh,
                "yellow": self.key_current_week,
                "blue": self.key_info,
                "left": self.key_left,
                "right": self.key_right,
                "ok": self.key_refresh,
            },
            -1,
        )

        self.onLayoutFinish.append(self.load_week)

    def key_left(self):
        self.week_offset -= 1
        self.load_week()

    def key_right(self):
        if self.week_offset < 0:
            self.week_offset += 1
            self.load_week()

    def key_refresh(self):
        self.app.service.clear_result_cache()
        self.load_week()

    def key_current_week(self):
        self.week_offset = 0
        self.load_week()

    def key_info(self):
        self.session.open(LottoInfoScreen)

    def load_week(self):
        try:
            view = self.app.service.get_week_view(self.week_offset)
        except Exception:
            self.session.open(MessageBox, _("Could not load draw data"), MessageBox.TYPE_ERROR, timeout=5)
            return

        self["week"].setText("KW %s/%s (%s - %s)" % (
            view.iso_week,
            view.iso_year,
            view.week_start.strftime("%d.%m.%Y"),
            view.week_end.strftime("%d.%m.%Y"),
        ))

        status_parts = []
        if self.week_offset == 0:
            status_parts.append(_("Current week"))
        if getattr(view, "status_hint", ""):
            status_parts.append(view.status_hint)
        self["status"].setText(" | ".join(status_parts))

        if len(view.games) < 2:
            self._clear_balls()
            self["e_row1_date"].setText("")
            self["e_row2_date"].setText("")
            self["l_row1_date"].setText("")
            self["l_row2_date"].setText("")
            return

        self._render_game_dates(view.games[0], "e_row1_date", "e_row2_date")
        self._render_game_dates(view.games[1], "l_row1_date", "l_row2_date")

        self._render_draw_balls(view.games[0], 0)
        self._render_draw_balls(view.games[0], 1)
        self._render_draw_balls(view.games[1], 2)
        self._render_draw_balls(view.games[1], 3)

    def _render_game_dates(self, game_data, first_name, second_name):
        first = game_data.draw_rows[0] if len(game_data.draw_rows) > 0 else None
        second = game_data.draw_rows[1] if len(game_data.draw_rows) > 1 else None

        self[first_name].setText(first.date_label if first else "")
        self[second_name].setText(second.date_label if second else "")

    def _render_draw_balls(self, game_data, ball_group_index):
        names = self.BALL_GROUPS[ball_group_index]
        draw_index = 0 if ball_group_index in (0, 2) else 1

        if draw_index >= len(game_data.draw_rows):
            for n in names:
                self[n].setText("")
            return

        row = game_data.draw_rows[draw_index]
        values = []
        values.extend(row.main_numbers)
        values.extend(row.special_numbers)

        idx = 0
        for n in names:
            if idx < len(values):
                self[n].setText(values[idx].rjust(2, "0"))
            else:
                self[n].setText("")
            idx += 1

    def _clear_balls(self):
        for group in self.BALL_GROUPS:
            for name in group:
                self[name].setText("")


class LottoInfoScreen(Screen):
    skin = """
        <screen name="LottoInfoScreen" position="center,90" size="1000,620" title="Lotto Info">
            <widget source="title" render="Label" position="20,10" size="960,35" font="Regular;30" />
            <widget name="body" position="20,55" size="690,500" font="Regular;24" scrollbarMode="showOnDemand" />
            <widget name="qr" position="740,100" size="240,240" alphatest="blend" />
            <widget source="support" render="Label" position="20,560" size="960,24" font="Regular;20" foregroundColor="#666666" />
            <ePixmap pixmap="skin_default/buttons/red.png" position="20,585" size="220,30" alphatest="on" />
            <widget source="key_red" render="Label" position="20,585" size="220,30" font="Regular;22" halign="center" valign="center" transparent="1" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self["title"] = StaticText(_("Information"))
        self["key_red"] = StaticText(_("Close"))
        self["support"] = StaticText("Buy me a coffee: https://buymeacoffee.com/madoe21")
        self["body"] = ScrollLabel(self._info_text())
        self["qr"] = Pixmap()
        self.onLayoutFinish.append(self._load_qr)

        self["actions"] = ActionMap(
            ["OkCancelActions", "DirectionActions", "ColorActions"],
            {
                "cancel": self.close,
                "ok": self.close,
                "red": self.close,
                "up": self["body"].pageUp,
                "down": self["body"].pageDown,
                "left": self["body"].pageUp,
                "right": self["body"].pageDown,
            },
            -1,
        )

    def _info_text(self):
        lines = [
            "LottoDE Plugin",
            "",
            _("Data source") + ": lotto.de",
            "",
            "LOTTO 6aus49, Eurojackpot",
            "",
            _("Controls") + ":",
            u"  Links/Rechts  \u2192 Woche wechseln",
            u"  Gr\u00fcn          \u2192 " + _("Refresh"),
            u"  Rot           \u2192 " + _("Close"),
            u"  Gelb          \u2192 " + _("Current week"),
            u"  Blau          \u2192 " + _("Information"),
            "",
            "Buy me a coffee: https://buymeacoffee.com/madoe21",
            "GitHub: https://github.com/madoe21/enigma2-lotto",
        ]
        return "\n".join(lines)

    def _load_qr(self):
        for path in [
            resolveFilename(SCOPE_PLUGINS, "Extensions/LottoDE/res/qr_buymeacoffee.png"),
            os.path.join(os.path.dirname(__file__), "res", "qr_buymeacoffee.png"),
        ]:
            if os.path.exists(path):
                try:
                    self["qr"].instance.setPixmapFromFile(path)
                    return
                except Exception:
                    pass

