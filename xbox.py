# Place this file in the folder ~/.config/ranger/colorschemes/
# and set the colorscheme in ~/.config/ranger/rc.conf as shown in next line
# set colorscheme xbox
#
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import (absolute_import, division, print_function)

from ranger.colorschemes.default import Default
from ranger.gui.color import green, red, yellow


class Scheme(Default):
    progress_bar_color = green

    def use(self, context):
        fg, bg, attr = Default.use(self, context)

        if context.directory and not context.marked and not context.link \
                and not context.inactive_pane:
            fg = green

        if context.in_titlebar and context.hostname:
            fg = red if context.bad else yellow

        return fg, bg, attr
