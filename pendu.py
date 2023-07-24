from tkinter import *
import xml.etree.ElementTree as ET
from xml.dom import minidom

fichierXML = "C:/xampp/htdocs/Python/Projets/Pendu/Project_Pendu/menu.xml"

window = Tk()
window.geometry('600x600')
window.resizable(0, 0)

# Chargement du fichier XML
structureXML = ET.parse(fichierXML)
nodeElement = minidom.parse(fichierXML)
belowEnsemble = nodeElement.getElementsByTagName('label')
ensemble = structureXML.getroot()

print(ensemble[1].attrib["categorie"])

navbar = Menu(window, background="#d9d9d9")
navbar_list = Menu(navbar, tearoff=0)

    
for element in ensemble:
    navbar.add_cascade(label = element.attrib['categorie'], menu = navbar_list)

for belowElement in belowEnsemble:
    belowNavbar = navbar_list.add_command(label = belowElement.firstChild.nodeValue)



window.config(menu = navbar)

window.mainloop()