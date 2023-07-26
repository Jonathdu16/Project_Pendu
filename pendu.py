from tkinter import *
import xml.etree.ElementTree as ET

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
    
# La première boucle sert à associer les categories à leurs labels et à intégrer les labels des sous-menues
for lowElement in ensemble.findall('menu'):
    category = lowElement.attrib["categorie"]

    if category not in low_menu_by_category:
        low_menu_by_category[category] = Menu(navbar, tearoff=0)

    navbar_list = low_menu_by_category[category]

    for belowElement in lowElement.findall('lien'):
        label_element = belowElement.find('label')
        if label_element is not None:
            navbar_list.add_command(label = label_element.text)

# La deuxième boucle sert à associer les categories à leurs labels
for category, low_menu in low_menu_by_category.items():

    navbar.add_cascade(label=category, menu=low_menu)

window.config(menu = navbar)

window.mainloop()