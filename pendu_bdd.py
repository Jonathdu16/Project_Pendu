import sqlite3

pendu_bdd = sqlite3.connect('pendu_bdd.sqlite')

pendu = pendu_bdd.cursor()

pendu.execute('CREATE TABLE IF NOT EXISTS mots (id INTEGER PRIMARY KEY, mot VARCHAR(50) NOT NULL)')
pendu.execute('CREATE TABLE IF NOT EXISTS themes (id INTEGER PRIMARY KEY, theme VARCHAR(50) NOT NULL)')
pendu.execute('CREATE TABLE IF NOT EXISTS mots_themes (id_theme INTEGER, id_mot INTEGER, FOREIGN KEY (id_theme) REFERENCES themes (id), FOREIGN KEY (id_mot) REFERENCES mots (id))')
pendu.execute('INSERT INTO mots (mot) VALUES ()')