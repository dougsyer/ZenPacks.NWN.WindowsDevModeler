__doc__="""WindowsDeviceMap

Uses WMI to map Windows OS & hardware information

"""

from ZenPacks.zenoss.WindowsMonitor.WMIPlugin import WMIPlugin
from Products.DataCollector.plugins.DataMaps import MultiArgs
from Products.ZenUtils.Utils import prepId
import re


class NewWindowsDeviceMap(WMIPlugin):

    maptype = "WindowsDeviceMap"

    domainrolemap = {0: "Stand Alone Workstation",
                     1: "Domain Member Workstation",
                     2: "Stand Alone Server",
                     3: "Domain Member Server",
                     4: "Domain Controller",
                     5: "Domain Controller - PDC Emulator",
                     6: "Unknown",
                    }

    def queries(self):
        return {
            "Win32_OperatingSystem": "select * from Win32_OperatingSystem",
            "Win32_SystemEnclosure": "select * from Win32_SystemEnclosure",
            "Win32_ComputerSystem": "select * from Win32_ComputerSystem",
        }

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        om = self.objectMap()

        for os in results["Win32_OperatingSystem"]:
            if re.search(r'Microsoft', os.manufacturer, re.I):
                os.manufacturer = "Microsoft"
                if '2003' in os.caption:
                    os.OSArchitecture = ""
                osfields = (os.caption, os.OSArchitecture, os.CSDVersion)
                msfullos = " ".join(map(str.strip, osfields))
            om.setOSProductKey = MultiArgs(msfullos, os.manufacturer)
            om.snmpSysName = os.csname
            om.snmpContact = os.registereduser
            break

        for e in results["Win32_SystemEnclosure"]:
            om.setHWTag = e.smbiosassettag.rstrip()
            om.setHWSerialNumber = e.serialnumber.rstrip()
            break

        for f in results["Win32_ComputerSystem"]:
            model = f.model
            if not model:
                model = "Unknown"
            manufacturer = f.manufacturer
            if not manufacturer:
                manufacturer = "Unknown"
            elif manufacturer == 'Compaq':
                manufacturer = "HP"
            elif re.search(r'Dell', manufacturer):
                manufacturer = "Dell"
            om.setHWProductKey = MultiArgs(model, manufacturer)
            if f.Domain:
                domain = f.Domain
            else:
                domain = "no domain"
            om.snmpLocation = "Windows Domain: " + f.Domain
            om.snmpDescr = "Server Role:  " + domainrolemap.get(int(f.domainRole), 6)

            break

        return om
