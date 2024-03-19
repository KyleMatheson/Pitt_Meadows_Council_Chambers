# Python Imports
#import socket

# Extron Library imports
from extronlib import event
from extronlib.interface import RelayInterface
from extronlib.device import ProcessorDevice
from extronlib.system import ProgramLog
from modules.ConnectionHandler import GetConnectionHandler

# Project imports
from modules import qsc_dsp_Q_Sys_Core_Series_v1_13_2_1 as DspModule
from modules import extr_Scaler_IN806_IN1808_Series_v1_1_6_0 as SwitcherModule
from modules import extr_switcher_SW_HD_4K_Series_v1_2_0_0 as SdiSwitcherModule
from modules import igen_switcher_Toggle_v1_0_2_0 as UsbSwitcherModule
from modules import epsn_vp_EB_CB_Pro_G7xxx_Series_v1_1_0_1 as ProjectorModule
from modules import shrp_display_PNE_Series_v1_0_6_0 as DisplayModule
from modules import ptz_camera_USB_SDI_G2_Series_v1_1_0_0 as CameraModule

# Define devices
Processor = ProcessorDevice('Processor')

Relay1 = RelayInterface(Processor, 'RLY01')
Relay2 = RelayInterface(Processor, 'RLY02')



### DSP ###
DSPInterface = DspModule.EthernetClass('192.168.1.2', 23, Model='Q-Sys Core 110f') 
DSP = GetConnectionHandler(DSPInterface, 'CallInProgress',pollFrequency=60) 

SwitcherInterface = SwitcherModule.EthernetClass('192.168.1.3', 23, Model='IN1806')
SwitcherInterface.devicePassword = 'A2WFVRF' 
Switcher = GetConnectionHandler(SwitcherInterface,'AutoSwitchMode',pollFrequency=60)

SdiSwitcherInterface = SdiSwitcherModule.EthernetClass('192.168.1.4', 23, Model='SW4 HD 4K PLUS')
SdiSwitcherInterface.devicePassword = 'A2WFVRF' 
SdiSwitcher = GetConnectionHandler(SwitcherInterface,'AutoSwitchMode',pollFrequency=60)

# # Create a TCP/IP socket
# UsbSwitcherSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Set the keepalive options
# UsbSwitcherSocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
# UsbSwitcherSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
# UsbSwitcherSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 3)
# UsbSwitcherSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)

# # Connect the socket to the port where the server is listening
# server_address = ('192.168.1.5', 23)  # replace with your server's IP and port
# UsbSwitcherSocket.connect(server_address)

UsbSwitcherInterface = UsbSwitcherModule.SerialOverEthernetClass('192.168.1.5',23) 
UsbSwitcher = GetConnectionHandler(UsbSwitcherInterface,'Power',pollFrequency=60)

ProjectorInterface = ProjectorModule.EthernetClass('192.168.1.5', 23, Model='EB-2255U')
Projector = GetConnectionHandler(ProjectorInterface,'Power',pollFrequency=60)

DisplayInterface1 = DisplayModule.EthernetClass('192.168.1.6', 23, Model='PNE-601')
Display1 = GetConnectionHandler(DisplayInterface1,'Power',pollFrequency=60)

DisplayInterface2 = DisplayModule.EthernetClass('192.168.1.7', 23, Model='PNE-601')
Display2 = GetConnectionHandler(DisplayInterface2,'Power',pollFrequency=60)

CameraInterface1 = CameraModule.EthernetClass('192.168.1.8', 23, Model='USB')
Camera1 = GetConnectionHandler(CameraInterface1,'Power',pollFrequency=60)

CameraInterface2 = CameraModule.EthernetClass('192.168.1.9', 23, Model='SDI')
Camera2 = GetConnectionHandler(CameraInterface2,'Power',pollFrequency=60)

CameraInterface3 = CameraModule.EthernetClass('192.168.1.10', 23, Model='USB')
Camera3 = GetConnectionHandler(CameraInterface3,'Power',pollFrequency=60)

CameraInterface4 = CameraModule.EthernetClass('192.168.1.11', 23, Model='SDI')
Camera4 = GetConnectionHandler(CameraInterface4,'Power',pollFrequency=60)


ProgramLog ('device_manager.py loaded', 'info')
