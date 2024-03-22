# Python imports

# Extron Library imports
from extronlib.system import ProgramLog

# Project imports
import devices
import ui.tlp

def Initialize():
    
    devices.DSP.Connect()
    devices.Switcher.Connect()
    devices.SdiSwitcher.Connect()
    #devices.UsbSwitcher.Connect()
    devices.Projector.Connect()
    devices.Display1.Connect()
    devices.Display2.Connect()
    #devices.Camera1.Connect()
    #devices.Camera2.Connect()
    #devices.Camera3.Connect()
    #devices.Camera4.Connect()

    ui.tlp.ClerkTLP.HideAllPopups()
    ui.tlp.ClerkTLP.ShowPage('00 - Splash')

    # Finish Initialize() with a print()
    print('System Initialized')
    ProgramLog ('system.py loaded', 'info')
