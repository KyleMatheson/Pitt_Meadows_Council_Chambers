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
from modules import epsn_vp_CB_EB_PU100xx_PU2010x_Series_v1_0_2_0 as ProjectorModule
from modules import shrp_display_LC_60C_xxLExxxU_Series_v1_0_7_0 as DisplayModule
from modules import ptz_camera_USB_SDI_G2_Series_v1_1_0_0 as CameraModule

# Define devices
Processor = ProcessorDevice('Processor')

### DSP ###
DSPInterface = DspModule.EthernetClass('192.168.10.13', 1702, Model='Q-Sys Core 110f') 
DSP = GetConnectionHandler(DSPInterface, 'DesignName',pollFrequency=60) 

SwitcherInterface = SwitcherModule.SSHClass('192.168.10.12', 22023, Credentials=('admin', 'SapphireAdmin'), Model='IN1808')
Switcher = GetConnectionHandler(SwitcherInterface,'AutoSwitchMode ',pollFrequency=60)

SdiSwitcherInterface = SdiSwitcherModule.SerialClass(Processor, 'COM1', Model='SW4 HD 4K PLUS')
SdiSwitcher = GetConnectionHandler(SdiSwitcherInterface,'AutoSwitchMode',pollFrequency=60)

UsbSwitcherInterface = UsbSwitcherModule.SerialOverEthernetClass('192.168.10.15',4999, Model='Toggle')
UsbSwitcher = GetConnectionHandler(UsbSwitcherInterface,'FirmwareVersion',pollFrequency=60)

ProjectorInterface = ProjectorModule.EthernetClass('192.168.10.41', 3629, Model='EB-PU1007W')
Projector = GetConnectionHandler(ProjectorInterface,'Power',pollFrequency=60)

DisplayInterface1 = DisplayModule.EthernetClass('192.168.10.42', 10002, Model='LC-80LE650U')
Display1 = GetConnectionHandler(DisplayInterface1,'Power',pollFrequency=60)

DisplayInterface2 = DisplayModule.EthernetClass('192.168.10.43', 10002, Model='LC-80LE650U')
Display2 = GetConnectionHandler(DisplayInterface2,'Power',pollFrequency=60)

CameraInterface1 = CameraModule.EthernetClass('192.168.10.31', 5678, Model='12X-SDI-G2')
Camera1 = GetConnectionHandler(CameraInterface1,'Power',pollFrequency=60)

CameraInterface2 = CameraModule.EthernetClass('192.168.10.32', 5678, Model='12X-SDI-G2')
Camera2 = GetConnectionHandler(CameraInterface2,'Power',pollFrequency=60)

CameraInterface3 = CameraModule.EthernetClass('192.168.10.33', 5678, Model='12X-SDI-G2')
Camera3 = GetConnectionHandler(CameraInterface3,'Power',pollFrequency=60)

CameraInterface4 = CameraModule.EthernetClass('192.168.10.34', 5678, Model='12X-SDI-G2')
Camera4 = GetConnectionHandler(CameraInterface4,'Power',pollFrequency=60)


ProgramLog ('device_manager.py loaded', 'info')
