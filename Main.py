# -*- coding: utf-8 -*-# For French language
"""Principal File to start the program """
import sys
import mysql.connector

from Categories import Category
from Products import Product
from Substituts import Substitut

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="mysql"  # name of base de données
            )
mycursor = Myconnection.cursor()

""" Use to  connect to server"""


def display_menu(head, options):
    """ We def  a  function to write a automaticly menu """
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
    """ Star the principal program """
    choice = 0
    category = Category(mycursor)  # Def class to create table category
    product = Product(mycursor)
    substitut = Substitut(mycursor)
    Myconnection.commit()
    while choice in range(0,4):
        choice = display_menu("Bonjour, Bienvenue sur OFF_Substitut:", [
            "Première utilisation, enregistrement du catalogue des catégories et"
            " produits",
            "Quel aliment souhaitez-vous remplacer ?",
            "Retrouver mes aliments substitués",
            "Quitter menu"
            ])
        if choice == 0:
            """Première utilisation, enregistrement du catalogue des catégories et"
               produits"""

            category.motor(mycursor)  # Def engine of table
            category.fill(mycursor)  #  Fill the table
            Myconnection.commit()
            product.motor(mycursor)
            product.strange_key(mycursor)  # Def strange key of table
            product.fill(mycursor)
            Myconnection.commit()
            substitut.motor(mycursor)
            substitut.strange_key(mycursor)
            Myconnection.commit()
            print("Les tables sont enregistrées dans la base de données mysql")

        if choice == 1:
            """ Quel aliment souhaitez-vous remplacer ?"""
            # category = Category()
            # product = Product()
            # substitut = Substitut()
            print('Bonjour, Bienvenue dans le catalogue des catégories:')
            mycursor.execute("SELECT * FROM mysql.MyTableCategories")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
            choice_category = input(
                " Faite votre choix en indiquant le numéro de la catégorie")
            print(choice_category)
            choice_name_myresult = myresult[int(choice_category)-1]
            choice_name_category = choice_name_myresult[1]
            # test print("la catégorie choisie est :",choice_name_category)
            print('Voici les produits possibles de cette catégorie:',
                  choice_name_category)
            sql = """SELECT id_product, Name_Product FROM mysql.MyTableProducts 
                  WHERE id_category = %s"""
            nb_category = (choice_category,)
            mycursor.execute(sql, nb_category)  # Display the table
            myresult = mycursor.fetchall()
            count = 0
            for x in myresult:
                if count == 0:
                    x_premier = x[0]  # determine the first value id of product
                count += 1
                print(x)
            choice_product = input(
                " Faite votre choix en indiquant le numéro du produit")
            choice_name_myresult = myresult[int(choice_product) - int(x_premier)]
            choice_name_product = choice_name_myresult[1]
            print("le produit choisi est :", choice_name_product)
            product.find_substitut(choice_category, choice_name_product)
            # Function to find a substitut of the product
            #  Test print(choice_name_product, x[0])
            choice_menu = display_menu("Que veux tu faire :", [
                "Enregistrer",
                "Quitter menu"])
            if choice_menu == 0:
                substitut.fill(mycursor, choice_name_product, x[0])
                # Save the résult in the table My.TableSubstitut
            elif choice_menu == 1:
                sys.exit()  # permet de quiter le programme

        if choice == 2:
            """ Retrouver mes aliments substitués """
            # category = Category()
            # product = Product()
            # substitut = Substitut()
            print("OK choix 2")
            sql = """SELECT mysql.MyTableSubstituts.name_a_substituer ,
            mysql.MyTableProducts.name_product,
            mysql.MyTableProducts.store,
            mysql.MyTableProducts.url_product
            FROM mysql.MyTableSubstituts
            INNER JOIN mysql.MyTableProducts
            ON mysql.MyTableSubstituts.id_product =
            mysql.MyTableProducts.id_product"""
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print("Le substitut de ", x[0], " est  ", x[1], " acheté chez : ",
                      x[2], ", visible sur le lien", x[3])
            Myconnection.commit()
        if choice == 3:
            sys.exit()  # permet de quiter le programme
    Myconnection.commit()