from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.widget import Widget 
from kivy.graphics import *
from itertools import product

class WhiteSquare(Widget):
    pass

class BlackSquare(Widget):
    pass

class CheckersGame(GridLayout):
    def make_board(self):
        for row, col in product(range(8), repeat = 2):
            if (row + col) % 2 == 0:
                self.add_widget(WhiteSquare())
            else:
                self.add_widget(BlackSquare())


class CheckersApp(App):
    def build(self):
        game = CheckersGame()
        game.make_board()
        return game

if __name__ == '__main__':
    CheckersApp().run()
