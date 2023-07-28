import sqlite3

pendu_bdd = sqlite3.connect('pendu_bdd.sqlite')

pendu = pendu_bdd.cursor()

pendu.execute('CREATE TABLE IF NOT EXISTS mots (id INTEGER PRIMARY KEY, mot VARCHAR(50) NOT NULL)')
pendu.execute('CREATE TABLE IF NOT EXISTS themes (id INTEGER PRIMARY KEY, theme VARCHAR(50) NOT NULL)')
pendu.execute('CREATE TABLE IF NOT EXISTS mots_themes (id_theme INTEGER, id_mot INTEGER, FOREIGN KEY (id_theme) REFERENCES themes (id), FOREIGN KEY (id_mot) REFERENCES mots (id))')
pendu.execute("""
CREATE TRIGGER check_id_the_mots_and_themes
BEFORE INSERT ON mots_themes
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN NEW.id_theme NOT IN (SELECT id FROM themes) THEN
            RAISE (ABORT, 'La contrainte a échoué. id_theme doit correspondre à un id existant dans themes.')
        WHEN NEW.id_mot NOT IN (SELECT id FROM mots) THEN
            RAISE (ABORT, 'La contrainte a échoué. id_mot doit correspondre à un id existant dans mots.')
    END;
END;
""")
# pendu.execute("INSERT INTO mots (mot) VALUES ('HTML'), ('SQL'), ('JAVASCRIPT'), ('PHP')")
# pendu.execute("INSERT INTO themes (theme) VALUES ('Languages'), ('Marque de voiture')")
# pendu.execute("INSERT INTO mots_themes (id, id) VALUES (1, 1), (1, 2)")
# pendu.execute("DELETE FROM mots WHERE id = 1;")
# pendu.execute("DELETE FROM mots_themes WHERE id_theme = 3;")
# pendu.execute("Drop table mots_themes;")
pendu_bdd.commit()
pendu.close()