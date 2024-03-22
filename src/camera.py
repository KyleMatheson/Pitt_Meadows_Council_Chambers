from extronlib import event
from extronlib.ui import Button
from extronlib.system import Wait, MESet

class CameraManager:
    def __init__(self, uiDeviceList, SdiSwitcherObject,
                CamObject1,CamObject2,CamObject3,CamObject4):
                
        self.uiDeviceList = uiDeviceList

        self.SdiSwitcherObject = SdiSwitcherObject

        self.CamObject1 = CamObject1
        self.CamObject2 = CamObject2
        self.CamObject3 = CamObject3
        self.CamObject4 = CamObject4
        self.PTZCam = None
            

        self.BtnStateList = ['Pressed', 'Released', 'Held','Tapped']
        self.HoldTime = 3

    
        self.BtnPTZUp       = [Button(UI_Device, 4021) for UI_Device in self.uiDeviceList]
        self.BtnPTZDown     = [Button(UI_Device, 4022) for UI_Device in self.uiDeviceList]
        self.BtnPTZLeft     = [Button(UI_Device, 4023) for UI_Device in self.uiDeviceList]
        self.BtnPTZRight    = [Button(UI_Device, 4024) for UI_Device in self.uiDeviceList]
        self.BtnPTZZoomIn   = [Button(UI_Device, 4025) for UI_Device in self.uiDeviceList]
        self.BtnPTZZoomOut  = [Button(UI_Device, 4026) for UI_Device in self.uiDeviceList]
    
        self.BtnCameraControlList = self.BtnPTZUp+self.BtnPTZDown+self.BtnPTZLeft+self.BtnPTZRight+self.BtnPTZZoomIn+self.BtnPTZZoomOut

        self.BtnCamera1Select = [Button(UI_Device, 4001) for UI_Device in self.uiDeviceList]
        self.BtnCamera2Select = [Button(UI_Device, 4002) for UI_Device in self.uiDeviceList]
        self.BtnCamera3Select = [Button(UI_Device, 4003) for UI_Device in self.uiDeviceList]
        self.BtnCamera4Select = [Button(UI_Device, 4004) for UI_Device in self.uiDeviceList]

        self.BtnTricasterToggle = [Button(UI_Device, 4005) for UI_Device in self.uiDeviceList]

        self.BtnCameraPreset1   = [Button(UI_Device, 4011) for UI_Device in self.uiDeviceList]
        self.BtnCameraPreset2   = [Button(UI_Device, 4012) for UI_Device in self.uiDeviceList]
        self.BtnCameraPreset3   = [Button(UI_Device, 4013) for UI_Device in self.uiDeviceList]

        self.BtnCameraSelectList = ([self.BtnCamera1Select[0], self.BtnCamera2Select[0], self.BtnCamera3Select[0], self.BtnCamera4Select[0]])

        self.BtnCameraSelectMESet = [
            MESet([self.BtnCamera1Select[0], self.BtnCamera2Select[0], self.BtnCamera3Select[0], self.BtnCamera4Select[0]])
        ]
 
        self.__initEvents__()
     
    def __initEvents__(self):
        @event(self.BtnPTZUp, self.BtnStateList)
        def PTZUpBtnEvent(button, state):
            #self.set_active_cam(button)
            if state == 'Pressed':
                button.SetState(1)
                self.PTZCam.Set('PanTilt', 'Up', {'Pan Speed': 12, 'Tilt Speed': 12})
            elif state == 'Released':
                button.SetState(0)
                self.PTZCam.Set('PanTilt', 'Stop', {'Pan Speed': 12, 'Tilt Speed': 12})
        
        @event(self.BtnPTZDown, self.BtnStateList)
        def PTZDownBtnEvent(button, state):
            #self.set_active_cam(button)
            if state == 'Pressed':
                button.SetState(1)
                self.PTZCam.Set('PanTilt', 'Down', {'Pan Speed': 12, 'Tilt Speed': 12})
            elif state == 'Released':
                button.SetState(0)
                self.PTZCam.Set('PanTilt', 'Stop', {'Pan Speed': 12, 'Tilt Speed': 12})
        
        @event(self.BtnPTZLeft, self.BtnStateList)
        def PTZLeftBtnEvent(button, state):
            if state == 'Pressed':
                #self.set_active_cam(button)
                button.SetState(1)
                self.PTZCam.Set('PanTilt', 'Left', {'Pan Speed': 12, 'Tilt Speed': 12})
            elif state == 'Released':
                button.SetState(0)
                self.PTZCam.Set('PanTilt', 'Stop', {'Pan Speed': 12, 'Tilt Speed': 12})
        
        @event(self.BtnPTZRight, self.BtnStateList)
        def PTZRightBtnEvent(button, state):
            if state == 'Pressed':
                #self.set_active_cam(button)
                button.SetState(1)
                self.PTZCam.Set('PanTilt', 'Right', {'Pan Speed': 12, 'Tilt Speed': 12})
            elif state == 'Released':
                button.SetState(0)
                self.PTZCam.Set('PanTilt', 'Stop', {'Pan Speed': 12, 'Tilt Speed': 12})
        
        @event(self.BtnPTZZoomIn, self.BtnStateList)
        def PTZZoomInBtnEvent(button, state):
            if state == 'Pressed':
                #self.set_active_cam(button)
                button.SetState(1)
                self.PTZCam.Set('Zoom', 'Tele', {'Zoom Speed': 7}) 
            elif state == 'Released':
                button.SetState(0)
                self.PTZCam.Set('Zoom', 'Stop', {'Zoom Speed': 7}) 
        
        @event(self.BtnPTZZoomOut, self.BtnStateList)
        def PTZZoomOutBtnEvent(button, state):
            if state == 'Pressed':
                #self.set_active_cam(button)
                button.SetState(1)
                self.PTZCam.Set('Zoom', 'Wide', {'Zoom Speed': 7})
            elif state == 'Released':
                button.SetState(0)
                self.PTZCam.Set('Zoom', 'Stop', {'Zoom Speed': 7})

        @event(self.BtnCameraSelectList, self.BtnStateList)
        def cameraSelectEvent(button, state):
            if button.ID == 4001:
                self.PTZCam  = self.CamObject1
                #self.SdiSwitcherObject.Set('Input', '1')
                for meset in self.BtnCameraSelectMESet:
                    meset.SetCurrent(0)
            elif button.ID == 4002:
                self.PTZCam  = self.CamObject2
                #self.SdiSwitcherObject.Set('Input', '2')
                for meset in self.BtnCameraSelectMESet:
                    meset.SetCurrent(1)
            elif button.ID == 4003:
                self.PTZCam  = self.CamObject3
                #self.SdiSwitcherObject.Set('Input', '3')
                for meset in self.BtnCameraSelectMESet:
                    meset.SetCurrent(2)
            elif button.ID == 4004:
                self.PTZCam  = self.CamObject4
                #self.SdiSwitcherObject.Set('Input', '4')
                for meset in self.BtnCameraSelectMESet:
                    meset.SetCurrent(3)

   
    def CameraPowerOn(self):
        self.CamObject1.Set('Power',"On")
        self.CamObject2.Set('Power',"On")
        self.CamObject3.Set('Power',"On")
        self.CamObject4.Set('Power',"On")
         
    def CameraPowerOff(self):
        self.CamObject1.Set('Power',"Off")
        self.CamObject2.Set('Power',"Off")
        self.CamObject3.Set('Power',"Off")
        self.CamObject4.Set('Power',"Off")
    
    def VideoFeedbackUpdate(self):
        self.switcherObject.SubscribeStatus('Input', None, self.SwitcherFeedbackHandler)
        print ('Feedback Update Sent to Switcher')

    def SwitcherFeedbackHandler(self, command, value, qualifier):
        if command == 'Input':
           #print('Input: ' + value)
            if value == '1':
                for meset in self.BtnCameraInputsMESet:
                    meset.SetCurrent(0)
            elif value == '2':
                for meset in self.BtnCameraInputsMESet:
                    meset.SetCurrent(1)
            elif value == '3':
                for meset in self.BtnCameraInputsMESet:
                    meset.SetCurrent(2)
            elif value == '4':
                for meset in self.BtnCameraInputsMESet:
                    meset.SetCurrent(3)
            else: pass         

       
        



                    
    
        


        


        


    
    
    

        



