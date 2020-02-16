import requests
import mysql.connector

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données

        )

mycursor = Myconnection.cursor()

"""We create class Catégory to translate the data from a file jason in a table
name MyTableCategories"""


class Category:
    def __init__(self):
        # create a table MytableCategories in base de données My_Table
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS My_Table.MyTableCategories (
        id_category INT AUTO_INCREMENT NOT NULL,
        name_category VARCHAR(100) NOT NULL,
        PRIMARY KEY (id_category)
        );
        """)
        mycursor.execute("""ALTER TABLE My_Table.MyTableCategories ENGINE = InnoDB""")
    #  Function to fill data in this table
    def fill(self):
        # We request the api OFF to save in Table the categories the 4 first
        r = requests.get('https://fr.openfoodfacts.org/categories.json')
        packages_json_categories = r.json()
        # we take in table  MyTableCatégories the categories
        for i in range(4, 9):
            data_categories = {
                "name_category": packages_json_categories['tags'][i]['name']
            }
            mycursor.execute(
                """INSERT INTO My_Table.MytableCategories (name_category)
                 VALUES(%(name_category)s)""", data_categories)
            Myconnection.commit()