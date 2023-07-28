import sys
from tkinter import *
from pendu_update_canevas
import json

class Quitter(object):

    def __init__(self, window):
        self.quitter = window.destroy()

    def quitter(self):
        self.quitter

class Appearance(object):

    def __init__(self, window):
        self.window_appearance = Tk()
        self.window_appearance.geometry('500x300')
        self.window_appearance.resizable(0, 0)
        self.window_appearance.title('Les graphisme du jeu')
        pendu_update_canevas.py

        with open('conf.json', 'r') as file:
            self.data = json.load(file)
    
    def update_canevas(self):
        print(self.data['canevas'])
    
    # def 
if __name__ == '__main__':
    window = Tk()
    window.geometry('1000x700')
    window.resizable(0, 0)
    window.title('Jeu du Pendu')
    main = Appearance(window)
    window.mainloop() 