from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Ciao Gerardo, l'app funziona!")

MyApp().run()
