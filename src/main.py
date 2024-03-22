# Python imports

# Extron Library Imports
from extronlib import Platform, Version
from extronlib.system import ProgramLog

print('ControlScript', Platform(), Version())

# Project imports
import variables
import devices
import ui.tlp
import system
import audio
import video
import camera

AudioManager_ = audio.AudioManager(ui.tlp.ClerkTLPs, devices.DSP) #send UI list to class init
VideoManager_ = video.VideoManager(ui.tlp.ClerkTLPs, devices.Switcher, devices.Projector, devices.Display1, devices.Display2) #send UI list to class init
CameraManager_ = camera.CameraManager(ui.tlp.ClerkTLPs, devices.SdiSwitcher, devices.Camera1, devices.Camera2, devices.Camera3, devices.Camera4) #send UI list to class init


system.Initialize()  # Call the system's Initialize method

ProgramLog ('main.py loaded', 'info')