import sqlite3
import random

class Bdd(object):

    def __init__(self, db_file):
        self.bdd = sqlite3.connect(db_file)
        self.cursor = self.bdd.cursor()
    
    def close(self):
        self.cursor.close()
        self.bdd.close()
    
class spaceWord(object):

    def __init__(self, db_file):
        self.connect_bdd = Bdd(db_file)
        self.select_Word_randomly()

    def select_Word_randomly(self):
        query = "SELECT mot FROM mots ORDER BY RANDOM() LIMIT 1"
        self.connect_bdd.cursor.execute(query)
        word = self.connect_bdd.cursor.fetchone()
        return word[0]

if __name__ == '__main__':
    db_file_name = "pendu_bdd.sqlite"
    word_game = spaceWord(db_file_name)
    random_word = word_game.select_Word_randomly()
    print("Mot sélectionné au hasard:", random_word)