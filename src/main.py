from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.widget import Widget 
from kivy.graphics import *

class WhiteSquare(Widget):
    pass

class BlackSquare(Widget):
    pass

class CheckersGame(GridLayout):
    def make_board(self):
        for i in range(0, 64):
            if i % 2 == 0:
                self.add_widget(BlackSquare())
            else:
                self.add_widget(WhiteSquare())   

class CheckersApp(App):
    def build(self):
        game = CheckersGame()
        game.make_board()
        return game

if __name__ == '__main__':
    CheckersApp().run()
