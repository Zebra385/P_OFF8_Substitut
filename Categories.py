import requests
import mysql.connector



class Category:
    def __init__(self, mycursor):
        self.mycursor = mycursor
        """ We create class Catégory to translate the data from a file jason
            in a table name MyTableCategories in my database mysql
        """
        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS mysql.MyTableCategories (
        id_category INT AUTO_INCREMENT NOT NULL,
        name_category VARCHAR(100) NOT NULL,
        PRIMARY KEY (id_category)
        );
        """)

    def motor(self, mycursor):

        """Definition the engine of my table"""
        self.mycursor.execute(
            """ALTER TABLE mysql.MyTableCategories ENGINE = InnoDB""")

    def fill(self, mycursor):
        """Function to fill data in this table"""
        # We request the api OFF to save in Table the categories the 4 first
        r = requests.get('https://fr.openfoodfacts.org/categories.json')
        packages_json_categories = r.json()
        # we take in table  MyTableCatégories the categories
        for i in range(4, 9):
            data_categories = {
                "name_category": packages_json_categories['tags'][i]['name']
            }
            self.mycursor.execute(
                """INSERT INTO mysql.MytableCategories (name_category)
                 VALUES(%(name_category)s)""", data_categories)

