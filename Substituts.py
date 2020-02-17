import mysql.connector

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="mysql"  # name of base de données
        )
mycursor = Myconnection.cursor()
"""              Use to  connect to server              """

class Substitut:
    def __init__(self):
        """We create class Substitut to translate the data from a file jason
           in a table name MyTableSubstituts
        """
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS mysql.MyTableSubstituts (
        id_substitut INT  AUTO_INCREMENT NOT NULL,
        name_a_substituer VARCHAR(100) NOT NULL,
        id_product INT NOT NULL,
        PRIMARY KEY (id_substitut)
        );
        """)

    def motor(self):
        """Definition the engine of my table"""
        mycursor.execute(
            """ALTER TABLE mysql.MyTableSubstituts ENGINE = InnoDB""")

    def strange_key(self):
        """Definition the strange key of my table"""
        mycursor.execute("""
                ALTER TABLE mysql.MyTableSubstituts ADD CONSTRAINT
                table_products_table_substituts_fk
                FOREIGN KEY (id_product)
                REFERENCES mysql.MyTableProducts (id_product)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION;
                """)

    def fill(self, product, nb):
        """Function to fill data in this table"""
        data_substituts = {
            "name_a_substituer": product,
            "id_product": nb
        }
        mycursor.execute(
            """INSERT INTO mysql.MyTableSubstituts (
               name_a_substituer, id_product)
               VALUES(%(name_a_substituer)s, %(id_product)s)""",
               data_substituts)
        Myconnection.commit()
