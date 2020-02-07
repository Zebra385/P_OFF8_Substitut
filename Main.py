# -*- coding: utf-8 -*-# For French language
import json
import sys
from sqlalchemy import create_engine, Column, Integer, Text, MetaData, Table,\
    select
import requests


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
            print("{} - {}".format(idx+1, option))
        choice = input("Quel est votre choix")
        try:
            option_nb = int(choice)
        except ValueError:  # On anticipe l'erreur
            print("Non, mauvais choix, vous vous êtes trompé")
            continue  # retourne au debut de la boucle

        if 0 < option_nb <= len(options):
            return option_nb
        print("Non, mauvais choix, vous vous êtes trompé")


""" We use qslalchely to create a table to downlaod  the substitut of food"""


# We must connect to base de données
engine = create_engine('sqlite://')
conn = engine . connect()

# We def and create our table
metadata = MetaData()
Table_Categories = Table(
    'Table_Category', metadata,
    Column('id', Integer, primary_key=True, autoincrement=1),
    Column('name_category', Text),
    Column('url', Text)
)

Table_Categories.create(bind=engine)

if __name__ == '__main__':
    id = 0
    choice = display_menu("Bonjour, Bienvenue sur OFF_Substitut:", [
        "Quel aliment souhaitez-vous remplacer ?",
        "Retrouver mes aliments substitués",
        "Quitter menu"
    ])
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
