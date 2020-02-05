# -*- coding: utf-8 -*-# For French language
import json
import sys
from sqlalchemy import create_engine, Column, Integer, Text, MetaData, Table, select
import requests


class Categorie:
    def __init__(self, **key_attribut):
        for attr_name, attr_value in key_attribut.items():
            setattr(self, attr_name, attr_value)
            # print(attr_name,attr_value)


""" We def a function to make a menu automaticly"""


def display_menu(options):
    print("Bonjour, Bienvenue sur OFF_Substitut:")
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


""" We use qslalchely t create a table to downlaod  the substitut of food"""

# We must connect to base de données
engine = create_engine('sqlite://')

# We def and create our table

metadata = MetaData()
messages = Table(
    'messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('message', Text),
)

messages.create(bind=engine)

if __name__ == '__main__':
    # on remplit la base de données
    # d'abord on inserre
    insert_message = messages.insert().values(message='Nutela')
    # puis on excecute la requete
    engine.execute(insert_message)
    choice = display_menu([
        "Quel aliment souhaitez-vous remplacer ?",
        "Retrouver mes aliments substitués",
        "Quitter menu"
    ])
    if choice == 1:
        print("option 1")
        # r = requests.get('https://fr.wiki.openfoodfacts.org/API/categories')
        # print(r.headers) # affiche  le  contenu des headers
        # print(r.headers['server'])# affiche le server
        for key_attribut in json.load(open("Categories_Aliment_France_OFF.json")):
            # , "r",  encoding="UTF-8")):
            categorie = Categorie(**key_attribut)
            # print(categorie)
    elif choice == 2:
        print("option 2")
        # interogeons nos données

        stmt = select([messages.c.message])
        message, = engine.execute(stmt).fetchone()
        print(message)
    elif choice == 3:
        sys.exit()  # permet de quiter le programme
