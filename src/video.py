from extronlib import event
from extronlib.ui import Button, Level, Label, Slider
from extronlib.system import MESet, ProgramLog, Wait

class VideoManager:
    def __init__(self, uiDeviceList,
                switcherObject, projectorObject, display1Object, display2Object):
                
        self.uiDeviceList = uiDeviceList

        self.switcherObject = switcherObject

        self.projectorObject = projectorObject
        self.display1Object = display1Object
        self.display2Object = display2Object
               
        self.BtnStateList = ['Pressed', 'Released']
        self.VolBtnStateList = ['Pressed', 'Released', 'Repeated']
        BtnRepeatTime = 0.2

        self.BtnClerkPC             = [Button(UiDevice, 3001) for UiDevice in self.uiDeviceList]
        self.BtnDeputyClerkPC       = [Button(UiDevice, 3002) for UiDevice in self.uiDeviceList]
        self.BtnStaffLaptop1        =  [Button(UiDevice, 3003) for UiDevice in self.uiDeviceList]
        self.BtnStaffLaptop2        =  [Button(UiDevice, 3004) for UiDevice in self.uiDeviceList]  
        
        self.BtnConferenceSelect    = [Button(UiDevice, 3011) for UiDevice in self.uiDeviceList]

        self.BtnProjectorPower      = [Button(UiDevice, 3021) for UiDevice in self.uiDeviceList]
        self.BtnDisplay1Power       = [Button(UiDevice, 3022) for UiDevice in self.uiDeviceList]
        self.BtnDisplay2Power       = [Button(UiDevice, 3023) for UiDevice in self.uiDeviceList]

        self.BtnVideoInputs = ([self.BtnClerkPC[0], self.BtnDeputyClerkPC[0], self.BtnStaffLaptop1[0], self.BtnStaffLaptop2[0]])
        
        self.BtnVideoInputsMESet = [
            MESet([self.BtnClerkPC[0], self.BtnDeputyClerkPC[0], self.BtnStaffLaptop1[0], self.BtnStaffLaptop2[0]])
        ]

        @Wait(20)
        def StartupWait():
            self.VideoFeedbackUpdate()
            self.Display1FeedbackUpdate()
            self.Display2FeedbackUpdate()
            self.ProjectorFeedbackUpdate()
            self.projectorObject.Set('Input', 'HDMI') 
            self.display1Object.Set('Input', 'HDMI 1')
            self.display2Object.Set('Input', 'HDMI 1')

        self.__initEvents__()
    
    def __initEvents__(self):
        @event(self.BtnVideoInputs,'Pressed')
        def BtnMuteListEvent(button, state):
            if button.ID == 3001:
                self.switcherObject.Set('Input', '2', {'Type': 'Audio/Video'}) 
            elif button.ID == 3002:
                self.switcherObject.Set('Input', '3', {'Type': 'Audio/Video'}) 
            elif button.ID == 3003:
                self.switcherObject.Set('Input', '4', {'Type': 'Audio/Video'}) 
            elif button.ID == 3004:
                self.switcherObject.Set('Input', '5', {'Type': 'Audio/Video'}) 
            else: pass

        @event(self.BtnProjectorPower,'Pressed')
        def BtnProjectorPowerEvent(button, state):
            if button.State == 1:
                self.projectorObject.Set('Power', 'Off')
                button.SetState(0)
            elif button.State == 0:
                self.projectorObject.Set('Power', 'On')
                button.SetState(1)

        @event(self.BtnDisplay1Power,'Pressed')
        def BtnDisplay1PowerEvent(button, state):
            if button.State == 1:
                self.display1Object.Set('Power', 'Off')
                button.SetState(0)
            elif button.State == 0:
                self.display1Object.Set('Power', 'On')
                button.SetState(1)

        @event(self.BtnDisplay2Power,'Pressed')
        def BtnDisplay2PowerEvent(button, state):
            if button.State == 1:
                self.display2Object.Set('Power', 'Off')
                button.SetState(0)
            elif button.State == 0:
                self.display2Object.Set('Power', 'On')
                button.SetState(1)

        @event(self.BtnConferenceSelect,'Pressed')
        def BtnConferenceSelectEvent(button, state):
            pass

    def VideoFeedbackUpdate(self):
        self.switcherObject.SubscribeStatus('Input', None, self.SwitcherFeedbackHandler)
        print ('Feedback Update Sent to Switcher')

    def SwitcherFeedbackHandler(self, command, value, qualifier):
        if command == 'Input':
           #print('Input: ' + value)
            if value == '2':
                for meset in self.BtnVideoInputsMESet:
                    meset.SetCurrent(0)
            elif value == '3':
                for meset in self.BtnVideoInputsMESet:
                    meset.SetCurrent(1)
            elif value == '4':
                for meset in self.BtnVideoInputsMESet:
                    meset.SetCurrent(2)
            elif value == '5':
                for meset in self.BtnVideoInputsMESet:
                    meset.SetCurrent(3)
            else: pass         

    def ProjectorFeedbackUpdate(self):
        self.projectorObject.SubscribeStatus('Power', None, self.ProjectorFeedbackHandler)
        print ('Feedback Update Sent to Projector')
    
    def ProjectorFeedbackHandler(self, command, value, qualifier):
        if command == 'Power':
            if value == 'On':
                for button in self.BtnProjectorPower:
                    button.SetState(1)
            elif value == 'Off':
                for button in self.BtnProjectorPower:
                    button.SetState(0)
            else: pass

    def Display1FeedbackUpdate(self):
        self.display1Object.SubscribeStatus('Power', None, self.Display1FeedbackHandler)
        print ('Feedback Update Sent to Display1')

    def Display1FeedbackHandler(self, command, value, qualifier):
        if command == 'Power':
            if value == 'On':
                for button in self.BtnDisplay1Power:
                    button.SetState(1)
            elif value == 'Off':
                for button in self.BtnDisplay1Power:
                    button.SetState(0)
            else: pass

    def Display2FeedbackUpdate(self):
        self.display2Object.SubscribeStatus('Power', None, self.Display2FeedbackHandler)
        print ('Feedback Update Sent to Display2')

    def Display2FeedbackHandler(self, command, value, qualifier):
        if command == 'Power':
            if value == 'On':
                for button in self.BtnDisplay2Power:
                    button.SetState(1)
            elif value == 'Off':
                for button in self.BtnDisplay2Power:
                    button.SetState(0)
            else: pass
                       
    def VideoShutdown(self):
        self.projectorObject.Set('Power', 'Off')
        self.display1Object.Set('Power', 'Off')
        self.display2Object.Set('Power', 'Off')
        self.switcherObject.Set('OutputMute', 'On', {'Output': 'HDMI Out'})
            
    def VideoStartup(self):
        self.display1Object.Set('Power', 'On')
        self.display2Object.Set('Power', 'On')
        self.switcherObject.Set('OutputMute', 'Off', {'Output': 'HDMI Out'})
        self.switcherObject.Set('Input', '3', {'Type': 'Audio/Video'})



    ProgramLog('video.py loaded', 'info')



        




            
