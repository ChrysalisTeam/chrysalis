# -*- coding: utf-8 -*-
"""
Wrapper around rst2pdf's "dotted_toc" extension, for recent reportlab versions.

The stock extension registers its onDraw callback with setattr() on the canvas,
but reportlab now looks callbacks up via canvas.getNamedCB(), so it crashes with
"Missing onDraw callback attribute 'drawTOCEntryEndX'". We register it properly too.

Used via "-e dotted_toc_compat" (rst2pdf adds the current directory to sys.path).
"""

from rst2pdf.extensions import dotted_toc

_original_wrap = dotted_toc.DottedTableOfContents.wrap


def _wrap_with_named_callback(self, availWidth, availHeight):
    result = _original_wrap(self, availWidth, availHeight)
    funcname = 'drawTOCEntryEnd%s' % self.toc_counter[0]
    if hasattr(self.canv, "setNamedCB"):
        self.canv.setNamedCB(funcname, getattr(self.canv, funcname))
    return result


dotted_toc.DottedTableOfContents.wrap = _wrap_with_named_callback
