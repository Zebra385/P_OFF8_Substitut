# -*- coding: utf-8 -*-# For French language
import json, pprint
import sys
import requests, mysql.connector


"""We create class Catégory to translate the data from a file jason in a table
name Table_categories"""


class Categorie:
    def __init__(self, i, **key_attribut):
        self_i = i
        for attr_name, attr_value in key_attribut.items():
            setattr(self, attr_name, attr_value)
            if attr_name == "name":
                # test print(attr_name,attr_value)
                value_name = attr_value
            if attr_name == "url":
                # Test print(attr_name,attr_value)
                value_url = attr_value
        ins = Table_Categories.insert()
        # We take data name et url in the table
        conn.execute(ins, id=self_i, name_category=value_name, url=value_url)


""" We def a function to make a menu automaticly"""


def display_menu(head, options):
    print(head)
    while True:
        for idx, option in enumerate(options):
            print("{} - {}".format(idx, option))
        choice = input("Quel est votre choix")
        try:
            option_nb = int(choice)
        except ValueError:  # On anticipe l'erreur
            print("Non, mauvais choix, vous vous êtes trompé")
            continue  # retourne au debut de la boucle

        if 0 <= option_nb <= len(options):
            return option_nb
        print("Non, mauvais choix, vous vous êtes trompé")


if __name__ == '__main__':
    id = 0
    choice = display_menu("Bonjour, Bienvenue sur OFF_Substitut:", [
        "Première utilisation, enregistrement du catalogue des catégories et"
        " produits",
        "Quel aliment souhaitez-vous remplacer ?",
        "Retrouver mes aliments substitués",
        "Quitter menu"
    ])
    if choice == 0:
        """ We use mysql.connector to create a function to create a table"""

        # We must connect to server
        Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données
        )
        print(Myconnection)
        # Then we can create the table MytableCategories
        mycursor = Myconnection.cursor()
        # create a table MytableCategories in base de données My_Table
        mycursor.execute(
            "CREATE TABLE MyTableCategories (id INT AUTO_INCREMENT PRIMARY KEY, Category VARCHAR(50))")
        # create a table MytableProducts in base de données My_Table
        mycursor.execute(
            "CREATE TABLE MyTableProducts (id INT AUTO_INCREMENT PRIMARY KEY, Category  VARCHAR(50), NameProduct VARCHAR(50), url VARCHAR(200))")

        # We request the api OFF to save in Table the categories(only the 4 first
        r=requests.get('https://fr.openfoodfacts.org/categories.json')
        packages_json_categories = r.json()
        # we take in table  MyTableCatégories the categories
        for i in range (4,9):
            data_categories = {
                "Category" : packages_json_categories['tags'][i]['name']
            }
            mycursor.execute(
                """INSERT INTO MytableCategories (Category) VALUES(%(Category)s)""",
                data_categories)
            Myconnection.commit()
            package_name = packages_json_categories['tags'][i]['name']
            package_url = f'https://fr.openfoodfacts.org/category/{package_name}/1.json'
            r = requests.get(package_url)
            package_json_product = r.json()
            for j in range(1, 10):
                data_products = {
                    "Category": packages_json_categories['tags'][i]['name'],
                    "NameProduct": package_json_product['products'][j]['product_name'],
                    "url": package_json_product['products'][j]['url']
                }
                mycursor.execute(
                    """INSERT INTO MytableProducts (Category, NameProduct, url) VALUES(%(Category)s,%(NameProduct)s,%(url)s)""",
                    data_products)
                Myconnection.commit()

        print("Les tables sont enregistrées dans la base de données My_Table")



    if choice == 1:
        # test print("option 1")
        for key_attribut in json.load(open("Categories_Aliment_France_OFF.json"
                                           )):
            # , "r",  encoding="UTF-8")):
            id += 1
            categorie = Categorie(id, **key_attribut)
        s = select([Table_Categories])
        result = conn.execute(s)
        # display_menu("Vous devez choisir maintenant le numèro d'une
        # catégorie:", result['name_category'])
        # To see the categories
        for row in result:
            print("id:", row['id'], "; catégorie:", row['name_category'])

    elif choice == 2:
        print("option 2")
        # Test
        # r = requests.get('https://fr.openfoodfacts.org/categorie/1.json')
        # donnees = json.dumps(r.json.products)
        # print(donnees)

        # interogeons nos données
        payload = {'products': '1', 'ingredients': '1'}
        r = requests.get("http://httpbin.org/get", params=payload)
        print(r.json())
    elif choice == 3:
        sys.exit()  # permet de quiter le programme
