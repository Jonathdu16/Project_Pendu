from tkinter import *
from random import randrange

class Pendu(object):

    def __init__(self, window, word = None):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.window = window
        self.tableau = [
            {'support': [10, 150, 50, 150]},
            {'poteau': [30, 150, 30, 30]},
            {'poutre': [30, 30, 125, 30]},
            {'jambe_de_force': [30, 75, 75, 30]},
            {'corde': [125, 30, 125, 50]},
            {'tete': [110, 50, 140, 80]},
            {'corps': [125, 80, 125, 110]},
            {'bras': [125, 90, 100, 100]},
            {'bras': [125, 90, 150, 100]},
            {'jambes': [125, 110, 100, 140]},
            {'jambes': [125, 110, 150, 140]}
        ]
        self.pointInit = 0
        self.index_element = 0
        self.word = word

        self.canevas = Canvas(self.window, width=600, height=700, background='light yellow')
        self.canevas.grid(row=0, column=0, padx=5, pady=5, rowspan=10)
        # self.place_in_grid(self.canevas, row=0, column=0, rowspan=0, columnspan=0, padx=0, pady=0)

        # self.tracer = Button(self.window, text='Suivant pour construire le pendu', command=self.element_suivant)
        # self.tracer.grid(row=0, column=1, padx=5, pady=5, columnspan=2)


        self.quitter = Button(self.window, text='Quitter', command=self.window.destroy)
        self.quitter.grid(row=1, column=1, padx=5, pady=5)

        self.keyboard(alphabet)

        self.canevas.bind("<KeyPress>", self.keyboard)
        self.canevas.focus_set()
    
    def element_suivant(self, event =None):
        if len(self.tableau) >= len(self.canevas.find_all()) :
            element = self.tableau[self.index_element]
            for key, value in element.items():
                if key == 'tete':
                    x1, y1, x2, y2 = value
                    self.canevas.create_oval(x1, y1, x2, y2, outline='blue', width=2)
                else:
                    self.canevas.create_line(value, fill='blue', width=2)
            self.index_element += 1
    
    def keyboard(self, alphabet, event = None):
        row_num = 3
        col_num = 2
        for letter in alphabet:
            self.button = Button(self.window, text=letter)
            self.button.grid(row=row_num, column=col_num, padx=5, pady=5)
            col_num += 1
            if col_num > 8:  # Number of buttons per row
                col_num = 2
                row_num += 1

    def checkWord(self):
        return self.word

if __name__ == '__main__':
    window = Tk()
    window.geometry('1000x700')
    window.resizable(0, 0)
    window.title('Jeu du Pendu')
    main = Pendu(window)
    window.mainloop()