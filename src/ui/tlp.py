# Python imports

# Extron Library imports
from extronlib.device import UIDevice
from extronlib import event 
from extronlib.ui import Button, Level, Slider
from extronlib.system import MESet, Timer, Wait, File, Clock
from extronlib.system import ProgramLog

# Project imports
import devices

# Define UI Objects

ClerkTLP = UIDevice('ClerkTLP')

ClerkTLPs = [ClerkTLP]

BtnStart               = [Button(UI_Device, 1001) for UI_Device in ClerkTLPs]
BtnShutdown            = [Button(UI_Device, 1099) for UI_Device in ClerkTLPs]
BtnShutdownConfirm     = [Button(UI_Device, 1098) for UI_Device in ClerkTLPs]
BtnShutdownCancel      = [Button(UI_Device, 1097) for UI_Device in ClerkTLPs]

BtnSubpageHome         = [Button(UI_Device, 1010) for UI_Device in ClerkTLPs]
BtnSubpageAudio        = [Button(UI_Device, 1011) for UI_Device in ClerkTLPs]
BtnSubpageVideo        = [Button(UI_Device, 1012) for UI_Device in ClerkTLPs]
BtnSubpageCamera       = [Button(UI_Device, 1013) for UI_Device in ClerkTLPs]
BtnSubpageOverflow     = [Button(UI_Device, 1014) for UI_Device in ClerkTLPs]

BtnSubpageListTLP =  ([BtnSubpageHome[0], BtnSubpageAudio[0], BtnSubpageVideo[0], BtnSubpageCamera[0], BtnSubpageOverflow[0]],)

BtnSubpageMESetList =      [
    MESet([BtnSubpageHome[0], BtnSubpageAudio[0], BtnSubpageVideo[0], BtnSubpageCamera[0], BtnSubpageOverflow[0]]),
                                 ]
for meset in BtnSubpageMESetList:
    meset.SetCurrent(0)

# Define UI Object Events
@event(BtnStart, 'Pressed')
def StartupEvent(button, state):
    SystemStart()
    
@event(BtnShutdown, 'Pressed')
def ShutdownEvent(button, state):
    for UI_device in ClerkTLPs:
        UI_device.ShowPopup('999 - Shutdown')

@event(BtnShutdownCancel, 'Pressed')
def ShutdownEvent(button, state):
    for UI_device in ClerkTLPs:
        UI_device.HidePopup('999 - Shutdown')

@event(BtnShutdownConfirm, 'Pressed')
def ShutdownEvent(button, state):
    for UI_device in ClerkTLPs:
        UI_device.HideAllPopups()
        UI_device.ShowPage('00 - Splash')
    SysShutdownConfirm()

def SysShutdownConfirm(self):
    devices.Projector.Set('Power', 'Off')
    devices.Display1.Set('Power', 'Off')
    devices.Display2.Set('Power', 'Off')
    devices.Camera1.Set('Power', 'Off')
    devices.Camera2.Set('Power', 'Off')
    devices.Camera3.Set('Power', 'Off')
    devices.Camera4.Set('Power', 'Off')

    RecallPreset(2, 'Presets')

def SystemStart(self):
    devices.Display1.Set('Power', 'On')
    devices.Display2.Set('Power', 'On')
    devices.Camera1.Set('Power', 'On')
    devices.Camera2.Set('Power', 'On')
    devices.Camera3.Set('Power', 'On')
    devices.Camera4.Set('Power', 'On')
    
    devices.Switcher.Set('Input', '1')

    RecallPreset(1, 'Presets')

    for UI_device in ClerkTLPs:
        UI_device.ShowPage('01 - Main')

def RecallPreset(self, preset, snapshotbank):
    loadtime = 1
    devices.DSP.Set('SnapshotLoad', preset, {'Load Time': loadtime, 'Bank': snapshotbank})

ProgramLog ('tlp.py loaded', 'info')