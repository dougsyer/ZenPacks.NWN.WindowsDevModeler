import logging
import Globals
import os
from Products.ZenModel.ZenPack import ZenPackBase
log = logging.getLogger("zen.NWNWindowsDevModeler")

class ZenPack(ZenPackBase):

    def install(self, app):
        ZenPackBase.install(self, app)

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        if not leaveObjects:
            pass
