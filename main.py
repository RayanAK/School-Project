from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string('''
<Recorder>
    orientation: 'vertical'
    Label:
        id: display_label
        text: '00:00'
    BoxLayout:
        size_hint: 1, .2
        TextInput:
            id: user_input
            text: '5'
            disabled: duration_switch.active == False 
            on_text: root.enforce_numeric()

        Switch:
            id: duration_switch

    BoxLayout:
        Button:
            size_hint: 0.5,0.3
            id: start_button
            text: 'Start Recording'
           
            on_release: root.manager.current = 'soundboard'

        Button:
            size_hint: 0.5,0.3
            id: stop_button
            text: 'Stop Recording'
           
            disabled: True
''')
class Recorder(Screen):
    pass

class SoundBoard(Screen):
    pass

class Credits(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Choix(Screen):
    pass



class TestApp(App):
    def build(self):
        self.sound = SoundLoader.load('KSHMR_Top_Loop_01.mp3')
        self.sound1 = SoundLoader.load('KSHMR_Top_Loop_02.mp3')
        self.sound2 = SoundLoader.load('KSHMR_Top_Loop_03.mp3')
        self.sound3 = SoundLoader.load('KSHMR_Top_Loop_04.mp3')
        self.sound4 = SoundLoader.load('KSHMR_Top_Loop_05.mp3')
        self.sound5 = SoundLoader.load('KSHMR_Top_Loop_06.mp3')
        self.sound6 = SoundLoader.load('KSHMR_Top_Loop_07.mp3')
        self.sound7 = SoundLoader.load('KSHMR_Tom_01.ogg')
        self.sound8 = SoundLoader.load('KSHMR_Tom_02.ogg')
        self.sound9 = SoundLoader.load('KSHMR_Tom_03.ogg')
        self.sound10 = SoundLoader.load('KSHMR_Tom_04.ogg')
        self.sound11 = SoundLoader.load('KSHMR_Tom_05.ogg')
        self.sound12 = SoundLoader.load('KSHMR_Tom_06.ogg')
        self.sound13 = SoundLoader.load('KSHMR_Tom_07.mp3')
        self.sound14 = SoundLoader.load('KSHMR_Tom_08.mp3')
        self.sound15 = SoundLoader.load('KSHMR_Tom_09.mp3')
        self.sound16 = SoundLoader.load('KSHMR_Tom_10.mp3')
        self.sound17 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound18 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound19 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound20 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound21 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound22 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound23 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound24 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound25 = SoundLoader.load('KSHMR_Tom_03.mp3')
        self.sound26 = SoundLoader.load('KSHMR_Tom_03.mp3')



        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Credits(name='credits'))
        sm.add_widget(SoundBoard(name='soundboard'))
        sm.add_widget(Recorder(name='recorder'))

        return sm

    def son(self):
        if self.sound:
            self.sound.play()
            self.sound.loop = True
    def son1(self):
        if self.sound1:
            self.sound1.play()
            self.sound1.loop = True
    def son2(self):
        if self.sound2:
            self.sound2.play()
            self.sound2.loop = True

    def son3(self):
        if self.sound3:
            self.sound3.play()
            self.sound3.loop = True
    def son4(self):
        if self.sound4:
            self.sound4.play()
            self.sound4.loop = True
    def son5(self):
        if self.sound5:
            self.sound5.play()
            self.sound5.loop = True
    def son6(self):
        if self.sound6:
            self.sound6.play()
            self.sound6.loop = True
    def son7(self):
        if self.sound7:
            self.sound7.play()
            self.sound7.loop = True
    def son8(self):
        if self.sound8:
            self.sound8.play()
            self.sound8.loop = True
    def son9(self):
        if self.sound9:
            self.sound9.play()
            self.sound9.loop = True

    def son10(self):
        if self.sound10:
            self.sound10.play()
            self.sound10.loop = True

    def son11(self):
        if self.sound11:
            self.sound11.play()
            self.sound11.loop = True

    def son12(self):
        if self.sound12:
            self.sound12.play()
            self.sound12.loop = True

    def son13(self):
        if self.sound13:
            self.sound13.play()
            self.sound13.loop = True

    def son14(self):
        if self.sound14:
            self.sound14.play()
            self.sound14.loop = True

    def son15(self):
        if self.sound15:
            self.sound15.play()
            self.sound15.loop = True
    def son16(self):
        if self.sound16:
            self.sound16.play()
            self.sound16.loop = True
    def stopson(self):
        if self.sound:
            self.sound.stop()
    def stopson1(self):
        if self.sound1:
            self.sound1.stop()
    def stopson2(self):
        if self.sound2:
            self.sound2.stop()

    def stopson3(self):
        if self.sound3:
            self.sound3.stop()
    def stopson4(self):
        if self.sound4:
            self.sound4.stop()
    def stopson5(self):
        if self.sound5:
            self.sound5.stop()
    def stopson6(self):
        if self.sound6:
            self.sound6.stop()
    def stopson7(self):
        if self.sound7:
            self.sound7.stop()

    def stopson8(self):
        if self.sound8:
            self.sound8.stop()
    def stopson9(self):
        if self.sound9:
            self.sound9.stop()

    def stopson10(self):
        if self.sound10:
            self.sound10.stop()

    def stopson11(self):
         if self.sound11:
            self.sound11.stop()


    def stopson12(self):
        if self.sound12:
            self.sound12.stop()

    def stopson13(self):
        if self.sound13:
            self.sound13.stop()

    def stopson14(self):
        if self.sound14:
            self.sound14.stop()

    def stopson15(self):
        if self.sound15:
            self.sound15.stop()

    def stopson16(self):
        if self.sound16:
            self.sound16.stop()


    def credits(self):
        return Label(text='ABDALLAH-KHODJA Rayene Sami')





if __name__ == "__main__":
    TestApp().run()
