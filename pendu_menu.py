from tkinter import *
from tkinter import messagebox
import xml.etree.ElementTree as ET
import pendu_command_menu

class PenduMenu:

    def __init__(self, window, files_XML):
        self.window = window

        self.navbar = Menu(self.window, background="#d9d9d9")
        self.low_menu_by_category = {}

        self.load_menu_from_xml(files_XML)
        self.build_menu()

    def load_menu_from_xml(self, files_XML):
        structureXML = ET.parse(files_XML)
        ensemble = structureXML.getroot()

        for lowElement in ensemble.findall('menu'):
            category = lowElement.attrib["categorie"]

            if category not in self.low_menu_by_category:
                self.low_menu_by_category[category] = Menu(self.navbar, tearoff=0)

            navbar_list = self.low_menu_by_category[category]

            for belowElement in lowElement.findall('lien'):
                label_element = belowElement.find('label')
                command_element = belowElement.find('command')
                if label_element is not None or command_element is not None:
                    method_name = command_element.text
                    navbar_list.add_command(label=label_element.text, command=lambda method=method_name: self.search_method(method))

    def build_menu(self):
        for category, low_menu in self.low_menu_by_category.items():
            self.navbar.add_cascade(label=category, menu=low_menu)
        self.window.config(menu=self.navbar)
    
    def search_method(self, method):
        try:
            self.command = getattr(pendu_command_menu, method) 
            self.command_instance = self.command(self.window)
        except AttributeError:
            messagebox.showerror('Erreur', 'Programme incomplet mais une mise à jour arrive, donc patientez cela va revenir')
        
if __name__ == '__main__':
    window = Tk()
    window.geometry('1000x700')
    window.resizable(0, 0)
    window.title('Jeu du Pendu')
    fichierXML = "C:/xampp/htdocs/Python/Projets/Pendu/Project_Pendu/menu.xml"
    main = PenduMenu(window, fichierXML)
    window.mainloop()  