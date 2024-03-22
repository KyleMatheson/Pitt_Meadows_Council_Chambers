from extronlib import event
from extronlib.ui import Button, Level, Label, Slider
from extronlib.system import MESet, ProgramLog, Wait

class AudioManager:
    def __init__(self, uiDeviceList,
                dspObject):
                
        self.uiDeviceList = uiDeviceList

        self.dspObject = dspObject
       
        self.BtnStateList = ['Pressed', 'Released']
        self.VolBtnStateList = ['Pressed', 'Released', 'Repeated']
        BtnRepeatTime = 0.2

        self.LvlWireless1            = [Slider(UiDevice, 2001) for UiDevice in self.uiDeviceList]
        self.BtnWireless1Mute        = [Button(UiDevice, 2002) for UiDevice in self.uiDeviceList]
        
        self.LvlWireless2            = [Slider(UiDevice, 2003) for UiDevice in self.uiDeviceList]
        self.BtnWireless2Mute        = [Button(UiDevice, 2004) for UiDevice in self.uiDeviceList]

        self.LvlAllMic               = [Slider(UiDevice, 2005) for UiDevice in self.uiDeviceList]
        self.BtnAllMicMute           = [Button(UiDevice, 2006) for UiDevice in self.uiDeviceList]
        
        self.LvlPresenterMic         = [Slider(UiDevice, 2007) for UiDevice in self.uiDeviceList]
        self.BtnPresenterMicMute     = [Button(UiDevice, 2008) for UiDevice in self.uiDeviceList] 

        self.LvlMedia                = [Slider(UiDevice, 2009) for UiDevice in self.uiDeviceList]
        self.BtnMediaMute            = [Button(UiDevice, 2010) for UiDevice in self.uiDeviceList]

        self.LvlUSBIn                = [Slider(UiDevice,  2011) for UiDevice in self.uiDeviceList]
        self.BtnUSBInMute            = [Button(UiDevice, 2012) for UiDevice in self.uiDeviceList]

        self.LvlOverflow             = [Slider(UiDevice,  2013) for UiDevice in self.uiDeviceList]
        self.BtnOverflowMute         = [Button(UiDevice, 2014) for UiDevice in self.uiDeviceList]

        self.LvlLobby                = [Slider(UiDevice, 2015) for UiDevice in self.uiDeviceList]
        self.BtnLobbyMute            = [Button(UiDevice, 2016) for UiDevice in self.uiDeviceList]
        
        self.AudioObjects = ["AllMics", "Wireless1", "Wireless2", "PresenterMic", "Media", "USBIn", "Overflow", "Lobby"]

        self.BtnMuteList =      self.BtnWireless1Mute+self.BtnWireless2Mute+self.BtnAllMicMute+self.BtnPresenterMicMute+self.BtnMediaMute+self.BtnUSBInMute+self.BtnLobbyMute
        
        self.BtnMuteStartupList =   self.BtnAllMicMute+self.BtnMediaMute+self.BtnUSBInMute
        
        self.LvlList =          self.LvlWireless1+self.LvlWireless2+self.LvlAllMic+self.LvlPresenterMic+\
                                self.LvlMedia+self.LvlUSBIn+self.LvlOverflow+self.LvlLobby

        self.MicLvlList =       self.LvlWireless1+self.LvlWireless2+self.LvlPresenterMic

        self.MicMasterList =    self.LvlAllMic
        
        self.ProgramLvlList =   self.LvlMedia+self.LvlUSBIn+self.LvlOverflow+self.LvlLobby  

        for lvl in self.MicLvlList:  #limit microphone range to 15dB
            lvl.SetRange(-15,0,1)
        for lvl in self.ProgramLvlList:  #limit program range to 30dB
            lvl.SetRange(-30,0,1)
        for lvl in self.MicMasterList:  #limit master microphone range to +/-3db
            lvl.SetRange(-3,3,1)

        for lvl in self.MicLvlList:
            lvl.SetFill(-5)
        
        for lvl in self.ProgramLvlList:
            lvl.SetFill(-10)
        
        for lvl in self.MicMasterList:
            lvl.SetFill(0)
        
        self.AudioStartup()
     
        self.__initEvents__()
    
    def __initEvents__(self):
        @event(self.BtnMuteList,'Pressed')
        def BtnMuteListEvent(button, state):
            if button.State == 0:
                self.dspObject.Set('Mute', 'On', {'Control ID': button.Name[:-5]+'Mute'})
                button.SetState(1)
            elif button.State == 1:
                self.dspObject.Set('Mute', 'Off', {'Control ID': button.Name[:-5]+'Mute'})
                button.SetState(0)
            @Wait(.25)
            def UpdateMute():
                self.MuteFeedback(button)

        @event(self.LvlList,'Changed')
        def LvlListEvent(slider, state, value):
            self.SetLevel(value, slider.Name[:-5])
            for lvl in self.LvlList:
                if slider.Name[:-5] == lvl.Name[:-5]:
                    lvl.SetFill(value)
            @Wait(.25)
            def UpdateLevel():
                self.LevelFeedback(slider)
        
    def SetLevel(self,level,controlID):
        self.dspObject.Set('Gain', level, {'Control ID': controlID+'Gain'}) 
   
    def MuteFeedback(self, button):
        value = self.dspObject.ReadStatus('Mute', {'Control ID': str(button.Name[:-5])+'Mute'})
        #print ("Mute FB Read & value is ", value)
        if value == 'On':
           button.SetState(1)
        elif value == 'Off':
              button.SetState(0)

    def LevelFeedback(self, slider):
        value = self.dspObject.ReadStatus('Gain', {'Control ID': str(slider.Name[:-5])+'Gain'})
        #print("DSP Level FB is ", value)
        for lvl in self.LvlList:
            if slider.Name[:-5] == lvl:
                lvl.SetFill(int(value))

    def RecallPreset(self, preset):
        snapshotbank = 'Presets'
        loadtime = 1
        self.dspObject.Set('SnapshotLoad', preset, {'Load Time': loadtime, 'Bank': snapshotbank})
        if preset == 1: #shutdown
            self.AudioShutdown()
        elif preset == 2: #startup
            self.AudioStartup()

    def AudioShutdown(self):
        for btn in self.BtnMuteList:
            btn.SetState(1)
            self.dspObject.Set('Mute', 'On', {'Control ID': btn.Name[:-5]+'Mute'})
            
    def AudioStartup(self):
        for btn in self.BtnMuteStartupList:
            btn.SetState(0)
            self.dspObject.Set('Mute', 'Off', {'Control ID': btn.Name[:-5]+'Mute'})
            

    ProgramLog('audio.py loaded', 'info')



        




            
