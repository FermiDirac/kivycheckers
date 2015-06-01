__author__ = 'Scott'
from kivy.app import App
from kivy.uix.widget import Widget

class CheckersGame(Widget):
    pass

class CheckersApp(App):
    def build(self):
        return CheckersGame()

if __name__ == '__main__':
    CheckersApp().run()
