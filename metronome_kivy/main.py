from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from os import listdir
from kivy.properties import StringProperty, DictProperty
from random import choice

from kivy.garden.roulette import Roulette, CyclicRoulette, TimeFormatCyclicRoulette
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class RockButton(Button):
    pass

class Metronome(Roulette):
    pass
    
class ScissorsButton(Button):
    pass

class PaperButton(Button):
    pass

class ResultScreen(Screen):
    pass

class Container(Screen):
    pass

class MainApp(App):
    # or string property idk
    def build(self):

        sm = ScreenManager()
        sm.add_widget(Container(name='main'))

        return sm

if __name__ == "__main__":
    app = MainApp()
    app.run()