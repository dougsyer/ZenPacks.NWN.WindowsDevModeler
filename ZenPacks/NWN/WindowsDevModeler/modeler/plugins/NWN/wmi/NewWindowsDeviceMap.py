__doc__="""WindowsDeviceMap

Uses WMI to map Windows OS & hardware information

"""

from Products.ZenWin.WMIPlugin import WMIPlugin
from Products.DataCollector.plugins.DataMaps import MultiArgs
from Products.ZenUtils.Utils import prepId
import re

class WindowsDeviceMap(WMIPlugin):

    maptype = "WindowsDeviceMap"

    def queries(self):
        return  {
            "Win32_OperatingSystem":"select * from Win32_OperatingSystem",
            "Win32_SystemEnclosure":"select * from Win32_SystemEnclosure",
        }

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        om = self.objectMap()

        for os in results["Win32_OperatingSystem"]:
            if re.search(r'Microsoft', os.manufacturer, re.I):
                os.manufacturer = "Microsoft"
                osfields = (os.caption, os.OSArchitecture, os.CSDVersion)
                msfullos = " ".join(map(str.strip, osfields))
            om.setOSProductKey = MultiArgs(msfullos, os.manufacturer)
            om.snmpSysName = os.csname # lies!
            om.snmpContact = os.registereduser # more lies!
            break

        for e in results["Win32_SystemEnclosure"]:
            om.setHWTag = e.smbiosassettag.rstrip()
            om.setHWSerialNumber = e.serialnumber.rstrip()
            break

        for f in results["Win32_ComputerSystem"]:
            model = f.model
            if not model: model = "Unknown"
            manufacturer = f.manufacturer
            if not manufacturer:
                manufacturer = "Unknown"
            elif manufacturer=='Compaq':
                manufacturer = "HP"
            elif re.search(r'Dell', manufacturer):
                manufacturer = "Dell"
            om.setHWProductKey = MultiArgs(model, manufacturer)
            break

        return om

