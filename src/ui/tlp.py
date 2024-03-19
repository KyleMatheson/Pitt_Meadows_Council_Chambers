"""
This is the place to put the modules for each UI in the system.  One module for each unique ui --
mirrored panels should be in the same file.
* UI object definition
* UI navigation
"""

# Python imports

# Extron Library imports
from extronlib.device import UIDevice
from extronlib.system import ProgramLog

# Project imports

# Define UI Objects

ClerkTLP = UIDevice('ClerkTLP')
ClerkVTLP = UIDevice('ClerkVTLP')

ClerkTLPs = [ClerkTLP, ClerkVTLP]


# Define UI Object Events


ProgramLog ('tlp.py loaded', 'info')