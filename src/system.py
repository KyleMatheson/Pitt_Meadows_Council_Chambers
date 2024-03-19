"""
The system is the place to define system logic, automation, services, etc. as a whole.  It should
provide an *Initialize* method that will be called in main to start the start the system after
variables, devices, and UIs have been defined.

Examples of items in the system file:
* Clocks and scheduled things
* Connection of devices that need connecting
* Set up of services (e.g. ethernet servers, CLIs, etc.)
"""

# Python imports

# Extron Library imports
from extronlib.system import ProgramLog

# Project imports
import devices

def Initialize():
    
    devices.DSP.Connect()
    devices.Switcher.Connect()
    devices.SdiSwitcher.Connect()
    devices.UsbSwitcher.Connect()
    devices.Projector.Connect()
    devices.Display1.Connect()
    devices.Display2.Connect()
    devices.Camera1.Connect()
    devices.Camera2.Connect()
    devices.Camera3.Connect()
    devices.Camera4.Connect()


    

    # Finish Initialize() with a print()
    print('System Initialized')
    ProgramLog ('system.py loaded', 'info')
