import mysql.connector

Myconnection = mysql.connector.connect(
            host="localhost",  # l'hote sera local
            user=" root ",
            database="My_table"  # name of base de données

        )

mycursor = Myconnection.cursor()

"""We create class Substitut to translate the data from a file jason in a table
name MyTableSubstituts"""


class Substitut:
    def __init__(self):

        # create a table MytableSubstituts in base de données My_Table
        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS My_Table.MyTableSubstituts (
        id_product INT NOT NULL,
        PRIMARY KEY (id_product)
        );
        """)
        mycursor.execute("""ALTER TABLE My_Table.MyTableSubstituts ENGINE = InnoDB""")
        mycursor.execute("""
        ALTER TABLE My_Table.MyTableSubstituts ADD CONSTRAINT table_products_table_substituts_fk
        FOREIGN KEY (id_product)
        REFERENCES My_Table.MyTableProducts (id_product)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION;
        """)
    #  Function to fill data in this table
    def fill(self):
        pass

