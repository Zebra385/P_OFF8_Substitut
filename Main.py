# -*- coding: utf-8 -*-# For French language
import sys
import requests
import mysql.connector

# We must connect to server
Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données

        )
print(Myconnection)
mycursor = Myconnection.cursor()


"""We create class Catégory to translate the data from a file jason in a table
name MyTableCategories"""


class Category:
    def __init__(self):
        # create a table MytableCategories in base de données My_Table
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS MyTableCategories(
        id INT AUTO_INCREMENT,
        name_category VARCHAR(50),
        PRIMARY KEY (id)
        );
        """)
        mycursor.execute("""ALTER TABLE MyTableCategories ENGINE = InnoDB""")
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
                """INSERT INTO MytableCategories (name_category)
                 VALUES(%(name_category)s)""", data_categories)
            Myconnection.commit()


"""We create class Product to translate the data from a file jason in a table
name MyTableProducts"""


class Product:
    def __init__(self):

        # Then we can create the table Mytableproducts
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS MyTableProducts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        NameProduct VARCHAR(100),
        url VARCHAR(200),
        nutriscore_grade VARCHAR(1),
        store VARCHAR(50),
        category_id INT
        );
        """)
        mycursor.execute("""ALTER TABLE MyTableProducts ENGINE = InnoDB""")
        mycursor.execute("""ALTER TABLE MyTableProducts ADD CONSTRAINT fk_name_category FOREIGN KEY (category_id) REFERENCES my_table.MyTableCategories(id)""")
    #  Function to fill data in this table
    def fill(self):
        mycursor.execute("SELECT * FROM MytableCategories")
        myresult = mycursor.fetchall()
        for x in myresult:
            # print(x[1])
            package_name = x[1]
            package_url = \
                f'https://fr.openfoodfacts.org/category/{package_name}/2.json'
            r = requests.get(package_url)
            package_json_product = r.json()
            for j in range(2, 11):
                try :
                    #  package_json_product['products'][j] = package_json_product['products'][j].get('nutriscore_grade', 'f') #  si le nustiscore n'existe pas
                    #  package_json_product['products'][j] = package_json_product['products'][j].get('stores', '?')   # si le storen'existe pas
                    data_products = {
                        "NameProduct": package_json_product['products'][j]['product_name'],
                        "nutriscore_grade": package_json_product['products'][j]['nutriscore_grade'],
                        "store" : package_json_product['products'][j]['stores'],
                        "url": package_json_product['products'][j]['url']
                    }

                    mycursor.execute(
                        """INSERT INTO MytableProducts (NameProduct, nutriscore_grade, store, url)
                        VALUES(%(NameProduct)s, %(nutriscore_grade)s, %(store)s, %(url)s)""",
                        data_products)
                    Myconnection.commit()
                except: # If key don't exist in the file json
                    continue
    #  Function to fin a sustit to the product
    def find_substitut(self,category,product):
        pass



"""We create class Substitut to translate the data from a file jason in a table
name MyTableSubstituts"""


class Substitut:
    def __init__(self):

        # create a table MytableSubstituts in base de données My_Table
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS MyTableSubstituts (
        id_substitut INT,
        CONSTRAINT fk_id_substitut  FOREIGN KEY (id_substitut) REFERENCES MyTableProducts(id)
        );
        """)
        mycursor.execute("""ALTER TABLE MyTableSubstituts ENGINE=InnoDB""")
    #  Function to fill data in this table
    def fill(self):
        pass


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
        category = Category()
        product = Product()
        substitut = Substitut()
        print('Bonjour, Bienvenue dans le catalogue des catégories:')
        mycursor.execute("SELECT * FROM MyTableCategories")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        choice_gategory = input(
            " Faite votre choix en indiquant le numéro de la catégorie")
        print(choice_gategory)
        choice_name_myresult = myresult[int(choice_gategory)-1]
        choice_name_category = choice_name_myresult[1]
        # test print("la catégorie choisie est :",choice_name_category)
        print('Voici les produits possibles de cette catégorie:')
        sql = "SELECT id, NameProduct FROM MyTableProducts" \
              " WHERE name_category = %s"
        name_category = (choice_name_category,)
        mycursor.execute(sql, name_category)
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
