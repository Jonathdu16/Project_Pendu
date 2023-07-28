from tkinter import *
from pendu_menu import PenduMenu as PM
from pendu_canevas import Pendu as PC
import xml.etree.ElementTree as ET
from pendu_connect import spaceWord as PW

fichierXML = "C:/xampp/htdocs/Python/Projets/Pendu/Project_Pendu/menu.xml"
bdd = "pendu_bdd.sqlite"

window = Tk()
window.geometry('1000x700')
window.resizable(0, 0)
window.title('Jeu du Pendu')

pendu_word = PW(bdd)

pendu_menu = PM(window, fichierXML)
pendu_canevas = PC(window, pendu_word.select_Word_randomly())
print(pendu_canevas.checkWord())

window.mainloop()