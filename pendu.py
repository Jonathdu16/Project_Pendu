from tkinter import *
import xml.etree.ElementTree as ET
from xml.dom import minidom

fichierXML = "C:/xampp/htdocs/Python/Projets/Pendu/Project_Pendu/menu.xml"

window = Tk()
window.geometry('600x600')
window.resizable(0, 0)
window.title('Jeu du Pendu')

# def 

# Chargement du fichier XML
structureXML = ET.parse(fichierXML)
ensemble = structureXML.getroot()

navbar = Menu(window, background="#d9d9d9")

low_menu_by_category = {}
    
for lowElement in ensemble.findall('menu'):
    categorie = lowElement.attrib["categorie"]

    if categorie not in low_menu_by_category:
        low_menu_by_category[categorie] = Menu(navbar, tearoff=0)

    navbar_list = low_menu_by_category[categorie]

    for belowElement in lowElement.findall('lien'):
        label_element = belowElement.find('label')
        if label_element is not None:
            navbar_list.add_command(label = label_element.text)

for categorie, sous_menu in low_menu_by_category.items():

    navbar.add_cascade(label=categorie, menu=sous_menu)

window.config(menu = navbar)

window.mainloop()