from extronlib import event
from extronlib.ui import Button, Level, Label, Slider
from extronlib.system import MESet, ProgramLog, Wait

class CameraManager:
    def __init__(self, uiDeviceList, SdiSwitcherObject,
                CamObject1,CamObject2,CamObject3,CamObject4):
                
        self.uiDeviceList = uiDeviceList

        self.SdiSwitcherObject = SdiSwitcherObject

        self.CamObject1 = CamObject1
        self.CamObject2 = CamObject2
        self.CamObject3 = CamObject3
        self.CamObject4 = CamObject4
       
        self.BtnStateList = ['Pressed', 'Released']
        self.VolBtnStateList = ['Pressed', 'Released', 'Repeated']
        BtnRepeatTime = 0.2

        self.BtnCamera1       = [Button(UiDevice, 4001) for UiDevice in self.uiDeviceList]
        self.BtnCamera2       = [Button(UiDevice, 4002) for UiDevice in self.uiDeviceList]
        self.BtnCamera3       = [Button(UiDevice, 4003) for UiDevice in self.uiDeviceList]
        self.BtnCamera4       = [Button(UiDevice, 4004) for UiDevice in self.uiDeviceList]
        self.BtnTricaster     = [Button(UiDevice, 4005) for UiDevice in self.uiDeviceList]

        self.BtnPreset1     = [Button(UiDevice, 4011) for UiDevice in self.uiDeviceList]
        self.BtnPreset2     = [Button(UiDevice, 4012) for UiDevice in self.uiDeviceList]
        self.BtnPreset3     = [Button(UiDevice, 4013) for UiDevice in self.uiDeviceList]

        self.BtnCameraUp    = [Button(UiDevice, 4021) for UiDevice in self.uiDeviceList]
        self.BtnCameraDown  = [Button(UiDevice, 4022) for UiDevice in self.uiDeviceList]
        self.BtnCameraLeft  = [Button(UiDevice, 4023) for UiDevice in self.uiDeviceList]
        self.BtnCameraRight = [Button(UiDevice, 4024) for UiDevice in self.uiDeviceList]
        self.BtnCameraZoomIn = [Button(UiDevice, 4025) for UiDevice in self.uiDeviceList]   
        self.BtnCameraZoomOut = [Button(UiDevice, 4026) for UiDevice in self.uiDeviceList]

        self.BtnCameraInputs = ([self.BtnCamera1[0], self.BtnCamera2[0], self.BtnCamera3[0], self.BtnCamera4[0]])

        self.BtnCameraInputsMESet = [
            MESet([self.BtnCamera1[0], self.BtnCamera2[0], self.BtnCamera3[0], self.BtnCamera4[0]])
        ]

        for meset in self.BtnCameraInputsMESet:
            meset.SetCurrent(0)

        self.BtnPresets = self.BtnPreset1+self.BtnPreset2+self.BtnPreset3

        self.BtnPresetsMESet = [
            MESet([self.BtnPreset1[0], self.BtnPreset2[0], self.BtnPreset3[0]])
        ]

        for meset in self.BtnPresetsMESet:
            meset.SetCurrent(0)
          

        self.BtnCameraControls = self.BtnCameraUp+self.BtnCameraDown+self.BtnCameraLeft+self.BtnCameraRight+self.BtnCameraZoomIn+self.BtnCameraZoomOut

     
        self.__initEvents__()
    
    def __initEvents__(self):
        @event(self.BtnCameraInputs,self.BtnStateList)
        def BtnCameraInputsEvent(button, state):
            if state == 'Pressed':
                if button.ID == 4021:
                    self.CamObject1.Set('PanTilt', 'Up')
            elif state == 'Released':
                if button.ID == 4021:
                    self.CamObject1.Set('PanTilt', 'Stop')

        

    def CameraShutdown(self):
        pass
    
    def CameraStartup(self):
        pass

    ProgramLog('camera.py loaded', 'info')



        




            
