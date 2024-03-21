"""
The main program entrance file.  The contents of this should be:
* Identification of the platform and version.
* imports of the project components
* Call to initialize the system
"""

# Python imports

# Extron Library Imports
from extronlib import Platform, Version
from extronlib.system import ProgramLog

print('ControlScript', Platform(), Version())

# Project imports
import variables
import devices
import ui.tlp
import control.av
import system
import audio

AudioManager_ = audio.AudioManager(ui.tlp.ClerkTLPs) #send UI list to class init
AudioManager_.addDspObj(devices.DSP) #append DSP object to the class


system.Initialize()  # Call the system's Initialize method

ProgramLog ('main.py loaded', 'info')