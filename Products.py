import requests
import mysql.connector

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données

        )

mycursor = Myconnection.cursor()
"""We create class Product to translate the data from a file jason in a table
name MyTableProducts"""


class Product:
    def __init__(self):

        # Then we can create the table Mytableproducts
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS My_Table.MyTableProducts(
        id_product INT AUTO_INCREMENT NOT NULL,
        id_category INT NOT NULL,
        Name_Product VARCHAR(100) NOT NULL,
        nutriscore VARCHAR(1) NOT NULL,
        store VARCHAR(50) NOT NULL,
        url_Product VARCHAR(200) NOT NULL,
        PRIMARY KEY (id_product, id_category)
        );
        """)
        mycursor.execute("""ALTER TABLE My_Table.MyTableProducts ENGINE = InnoDB""")
        mycursor.execute("""
        ALTER TABLE My_Table.MyTableProducts ADD CONSTRAINT table_categories_table_products_fk
        FOREIGN KEY (id_category)
        REFERENCES My_Table.MyTableCategories (id_category)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION;
        """)
    #  Function to fill data in this table
    def fill(self):
        mycursor.execute("SELECT * FROM My_Table.MytableCategories")
        myresult = mycursor.fetchall()
        for x in myresult:
            package_name = x[1]
            package_url = \
                f'https://fr.openfoodfacts.org/category/{package_name}/2.json'
            r = requests.get(package_url)
            package_json_product = r.json()
            for j in range(2, 11):
                try :
                    data_products = {
                        "id_category": x[0],
                        "Name_Product": package_json_product['products'][j]['product_name'],
                        "nutriscore": package_json_product['products'][j]['nutriscore_grade'],
                        "store" : package_json_product['products'][j]['stores'],
                        "url_Product": package_json_product['products'][j]['url']
                    }

                    mycursor.execute(
                        """INSERT INTO My_Table.MyTableProducts (id_category, Name_Product, nutriscore, store, url_Product)
                        VALUES(%(id_category)s, %(Name_Product)s, %(nutriscore)s, %(store)s, %(url_Product)s)""",
                        data_products)
                    Myconnection.commit()
                except: # If key don't exist in the file json
                    continue

    #  Function to fin a sustit to the product
    def find_substitut(self,category,product):
        pass


