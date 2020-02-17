import requests
import mysql.connector

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données
        )
mycursor = Myconnection.cursor()
"""              Use to  connect to server              """

class Product:
    def __init__(self):
        """ We create class Product to translate the data from a file jason
                  in a table name MyTableProduct in my database My_Table
              """
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

    def motor(selfs):
        """Definition the engine of my table"""
        mycursor.execute(
            """ALTER TABLE My_Table.MyTableProducts ENGINE = InnoDB""")

    def strange_key(selfs):
        """Definition the strange key of my table"""
        mycursor.execute("""
                ALTER TABLE My_Table.MyTableProducts ADD CONSTRAINT
                table_categories_table_products_fk
                FOREIGN KEY (id_category)
                REFERENCES My_Table.MyTableCategories (id_category)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION;
                """)

    def fill(self):
        """Function to fill data in this table"""
        mycursor.execute("SELECT * FROM My_Table.MytableCategories")
        myresult = mycursor.fetchall()
        for x in myresult:
            package_name = x[1]
            package_url = \
                f'https://fr.openfoodfacts.org/category/{package_name}/2.json'
            r = requests.get(package_url)
            package_json_product = r.json()
            for j in range(2, 20):
                try:  # If key don't exist in the file json
                    #  to avoid mystake
                    data_products = {
                        "id_category": x[0],
                        "Name_Product": package_json_product['products'][j]
                        ['product_name'], "nutriscore": package_json_product
                        ['products'][j]['nutriscore_grade'],
                        "store": package_json_product['products'][j]['stores'],
                        "url_Product": package_json_product['products'][j]['url']
                    }
                    mycursor.execute("""
                        INSERT INTO My_Table.MyTableProducts (id_category,
                        Name_Product, nutriscore, store, url_Product)
                        VALUES(%(id_category)s, %(Name_Product)s,
                        %(nutriscore)s, %(store)s, %(url_Product)s)""",
                        data_products)
                    Myconnection.commit()
                except:
                    continue
                    # If a mystacke is detect you go at the begining of the loop

    def find_substitut(self, nb_category, leproduct):
        """Function to find a sustitut to the product
            simply you take the better key nutriscore
            it returns the name of substitut"""
        self.leproduct = leproduct
        sql = """SELECT id_product,id_category,Name_Product, nutriscore
                    FROM My_Table.MyTableProducts
                    WHERE id_category =%s
                    ORDER BY nutriscore
                    LIMIT 1"""
        nb = (nb_category,)
        mycursor.execute(sql, nb)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("le produit qui se substitut le mieux à :",
                  leproduct, 'est ', x[2])
            return x[0]
