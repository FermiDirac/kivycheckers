from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.button import Button 
from kivy.graphics import *
from itertools import product

class WhitePiece(Widget):
    pass

class RedPiece(Widget):
    pass

class Square(BoxLayout):
    pass

class CheckersGame(GridLayout):
    def make_board(self):
        for i in range(64):
            self.add_widget(Square())
        for row, col in product(range(8), repeat = 2):
            if (row + col) % 2 == 0 and row not in (3, 4):
                if (row * 8 + col) < 23:
                    self.children[row*8 + col].add_widget(WhitePiece())
                else:
                    self.children[row*8 + col].add_widget(RedPiece())


class CheckersApp(App):
    def build(self):
        game = CheckersGame()
        game.make_board()
        return game

if __name__ == '__main__':
    CheckersApp().run()
