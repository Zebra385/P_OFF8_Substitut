# -*- coding: utf-8 -*-# For French language
import sys
import mysql.connector
from Categories import Category
from Products import Product
from Substituts import Substitut

# We must connect to server
Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données

        )

mycursor = Myconnection.cursor()


"""We de a  function to write a automaticly menu"""


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


""" Star this program like the principal program """


if __name__ == '__main__':
    choice = display_menu("Bonjour, Bienvenue sur OFF_Substitut:", [
        "Première utilisation, enregistrement du catalogue des catégories et"
        " produits",
        "Quel aliment souhaitez-vous remplacer ?",
        "Retrouver mes aliments substitués",
        "Quitter menu"
        ])
    if choice == 0:
        """ We use mysql.connector to create a function to create a table"""
        category = Category()
        category.fill()
        product = Product()
        product.fill()
        substitut = Substitut()

        print("Les tables sont enregistrées dans la base de données My_Table")

    if choice == 1:

        print('Bonjour, Bienvenue dans le catalogue des catégories:')
        mycursor.execute("SELECT * FROM My_Table.MyTableCategories")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        choice_gategory = input(
            " Faite votre choix en indiquant le numéro de la catégorie")
        print(choice_gategory)
        choice_name_myresult = myresult[int(choice_gategory)-1]
        choice_name_category = choice_name_myresult[1]
        # test print("la catégorie choisie est :",choice_name_category)
        print('Voici les produits possibles de cette catégorie:', choice_name_category)
        sql = "SELECT id_product, Name_Product FROM My_Table.MyTableProducts" \
              " WHERE id_category = %s"
        nb_category = (choice_gategory,)
        mycursor.execute(sql, nb_category)
        myresult = mycursor.fetchall()
        count = 0
        for x in myresult:
            if count == 0:
                x_premier = x[0]  # determine the first value id of product
            print(x)
            count += 1
        choice_product = input(
            " Faite votre choix en indiquant le numéro du produit")
        choice_name_myresult = myresult[int(choice_product) - int(x_premier)]
        choice_name_product = choice_name_myresult[1]
        print("le produit choisi est :", choice_name_product)
    elif choice == 2:
        pass
    elif choice == 3:
        sys.exit()  # permet de quiter le programme
