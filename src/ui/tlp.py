# Python imports

# Extron Library imports
from extronlib.device import UIDevice
from extronlib import event 
from extronlib.ui import Button, Level, Slider
from extronlib.system import MESet, Timer, Wait, File, Clock
from extronlib.system import ProgramLog
import audio 
import video 
import camera 

# Project imports
import devices

# Define UI Objects

ClerkTLP = UIDevice('ClerkTLP')

ClerkTLPs = [ClerkTLP]

AudioManager_ = audio.AudioManager(ClerkTLPs, devices.DSP) #send UI list to class init
VideoManager_ = video.VideoManager(ClerkTLPs, devices.Switcher, devices.Projector, devices.Display1, devices.Display2) #send UI list to class init
CameraManager_ = camera.CameraManager(ClerkTLPs, devices.SdiSwitcher, devices.Camera1, devices.Camera2, devices.Camera3, devices.Camera4)

BtnStart               = [Button(UI_Device, 1001) for UI_Device in ClerkTLPs]
BtnShutdown            = [Button(UI_Device, 1099) for UI_Device in ClerkTLPs]
BtnShutdownConfirm     = [Button(UI_Device, 1098) for UI_Device in ClerkTLPs]
BtnShutdownCancel      = [Button(UI_Device, 1097) for UI_Device in ClerkTLPs]

BtnSubpageHome         = [Button(UI_Device, 1010) for UI_Device in ClerkTLPs]
BtnSubpageAudio        = [Button(UI_Device, 1011) for UI_Device in ClerkTLPs]
BtnSubpageVideo        = [Button(UI_Device, 1012) for UI_Device in ClerkTLPs]
BtnSubpageCamera       = [Button(UI_Device, 1013) for UI_Device in ClerkTLPs]
BtnSubpageOverflow     = [Button(UI_Device, 1014) for UI_Device in ClerkTLPs]

BtnSubpageListTLP =  ([BtnSubpageHome[0], BtnSubpageAudio[0], BtnSubpageVideo[0], BtnSubpageCamera[0], BtnSubpageOverflow[0]])

BtnSubpageMESetList =      [
    MESet([BtnSubpageHome[0], BtnSubpageAudio[0], BtnSubpageVideo[0], BtnSubpageCamera[0], BtnSubpageOverflow[0]]),
                                 ]
for meset in BtnSubpageMESetList:
    meset.SetCurrent(0)

# Define UI Object Events
@event(BtnStart, 'Pressed')
def StartupEvent(button, state):
    for UI_device in ClerkTLPs:
        UI_device.ShowPage("01 - Main")
        UI_device.ShowPopup('Home')
    for meset in BtnSubpageMESetList:
        meset.SetCurrent(0)
    audio.AudioManager.AudioStartup(AudioManager_)
    video.VideoManager.VideoStartup(VideoManager_)
    #camera.CameraManager.CameraStartup(CameraManager_)

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
    audio.AudioManager.AudioShutdown(AudioManager_)
    video.VideoManager.VideoShutdown(VideoManager_)
    #camera.CameraManager.CameraShutdown(CameraManager_)


@event(BtnSubpageListTLP, 'Pressed')
def SubpageButtonEvent(button, state):
    if button in BtnSubpageListTLP:
        index = BtnSubpageListTLP.index(button)
        for meset in BtnSubpageMESetList:
            meset.SetCurrent(index)
    if button.ID == 1010:
        for UI_device in ClerkTLPs:
            UI_device.ShowPopup('Home')
    elif button.ID == 1011:
        for UI_device in ClerkTLPs:
            UI_device.ShowPopup('Audio')
    elif button.ID == 1012:
        for UI_device in ClerkTLPs:
            UI_device.ShowPopup('Video')
    elif button.ID == 1013:
        for UI_device in ClerkTLPs:
            UI_device.ShowPopup('Cameras')
    elif button.ID == 1014:
        for UI_device in ClerkTLPs:
            UI_device.ShowPopup('Overflow')
    else: pass


ProgramLog ('tlp.py loaded', 'info')