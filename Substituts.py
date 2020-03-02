

class Substitut:
    def __init__(self, mycursor):
        self.mycursor = mycursor
        """We create class Substitut to translate the data from a file jason
           in a table name MyTableSubstituts
        """
        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS mysql.MyTableSubstituts (
        id_substitut INT  AUTO_INCREMENT NOT NULL,
        name_a_substituer VARCHAR(100) NOT NULL,
        id_product INT NOT NULL,
        PRIMARY KEY (id_substitut)
        );
        """)

    def motor(self, mycursor):
        """Definition the engine of my table"""
        self.mycursor.execute(
            """ALTER TABLE mysql.MyTableSubstituts ENGINE = InnoDB""")

    def strange_key(self, mycursor):
        """Definition the strange key of my table"""
        self.mycursor.execute("""
                ALTER TABLE mysql.MyTableSubstituts ADD CONSTRAINT
                table_products_table_substituts_fk
                FOREIGN KEY (id_product)
                REFERENCES mysql.MyTableProducts (id_product)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION;
                """)

    def fill(self, mycursor, product, nb):
        self.mycursor = mycursor
        """Function to fill data in this table"""
        data_substituts = {
            "name_a_substituer": product,
            "id_product": nb
        }
        self.mycursor.execute(
            """INSERT INTO mysql.MyTableSubstituts (
               name_a_substituer, id_product)
               VALUES(%(name_a_substituer)s, %(id_product)s)""",
            data_substituts)
