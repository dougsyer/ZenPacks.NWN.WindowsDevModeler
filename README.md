ZenPacks.NWN.WindowsDevModeler
==============================

This is a **slightly** improved Windows device modeller, to use, just remove the default Zenoss Windows replace core zenoss wmi plugin with this one

Features
=============================

- Correctly models system make and model using Win32_ComputerSystemClass.
- Adds in the platform (32/64 bit) and service pack level of the OS to the OS Model
    format is like this:
            Microsoft Windows Server 2008 R2 Standard 64-bit Service Pack 1
- Vmware guests should model as VmwareVirtualPlatorm, HyperV and Citrix/Xen guests should also work
- Added Windows Domain name to SNMP-location field
- Adds Server role to the SNMP Description field (domain controller, workstation, if its a pdc emulator)

This isnt ready yet, just transferring the code over now


Use
=============================
Install the zenpack, the egg should be in the /dist directory

Under appropriate device class/devices replace your default Zenoss WindowsDeviceMap modeller with this one or have it run after the Zenoss modeller

This is a WMI based plugin so you will need windows user/domain/password as with the other wmi modelers

Requirements
=============================
This Zenpack was tested in Zenoss Entperise 4.23, I would imagine it would work fine in core also.  It wont work in 4.1.1 without modfication to the WMI import statement in the modeller

Ive tested this on Windows 2008/R2 & 2003, all bets are off for older versions, havent tried 2012 yet

Future
============================
Add other windows roles
Look up other AD roles and add
Add javascript override to rename SNMP fields