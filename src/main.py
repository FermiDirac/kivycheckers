from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.widget import Widget 
from kivy.uix.button import Button
from kivy.graphics import *

class CheckersSquare(Widget):
    pass

class CheckersGame(GridLayout):
    def __init__(self):
        super(CheckersGame, self).__init__()
        self.cols = 8

    def make_board(self):
        for i in range(64):
            self.add_widget(CheckersSquare())

class CheckersApp(App):
    def build(self):
        game = CheckersGame()
        game.make_board()
        return game

if __name__ == '__main__':
    CheckersApp().run()
