import mysql.connector

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données
        )
mycursor = Myconnection.cursor()
"""              Use to  connect to server              """

class Substitut:
    def __init__(self):
        """We create class Substitut to translate the data from a file jason
           in a table name MyTableSubstituts
        """
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS My_Table.MyTableSubstituts (
        id_substitut INT  AUTO_INCREMENT NOT NULL,
        name_a_substituer VARCHAR(100) NOT NULL,
        id_product INT NOT NULL,
        PRIMARY KEY (id_substitut)
        );
        """)

    def motor(self):
        """Definition the engine of my table"""
        mycursor.execute(
            """ALTER TABLE My_Table.MyTableSubstituts ENGINE = InnoDB""")

    def strange_key(self):
        """Definition the strange key of my table"""
        mycursor.execute("""
                ALTER TABLE My_Table.MyTableSubstituts ADD CONSTRAINT
                table_products_table_substituts_fk
                FOREIGN KEY (id_product)
                REFERENCES My_Table.MyTableProducts (id_product)
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
            """INSERT INTO My_Table.MyTableSubstituts (
               name_a_substituer, id_product)
               VALUES(%(name_a_substituer)s, %(id_product)s)""",
               data_substituts)
        Myconnection.commit()
