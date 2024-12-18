import pyodbc
import mysql.connector
from mysql.connector import errorcode

class DataTransferService:
    def __init__(self, access_db_path, mysql_config):
        # Configura Access
        self.access_conn_str = f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_db_path};"
        try:
            self.access_conn = pyodbc.connect(self.access_conn_str)
            self.access_cursor = self.access_conn.cursor()
            print("Connesso al database Access.")
        except pyodbc.Error as err:
            print(f"Errore di connessione a Access: {err}")
            raise

        # Configura MySQL
        try:
            self.mysql_conn = mysql.connector.connect(**mysql_config)
            self.mysql_cursor = self.mysql_conn.cursor()
            print("Connesso al database MySQL.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Errore di autenticazione MySQL.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database MySQL non trovato.")
            else:
                print(f"Errore MySQL: {err}")
            raise

    def create_table_from_access(self, table_name):
        """
        Crea una tabella in MySQL basata sulla struttura della tabella Access.
        """
        self.access_cursor.execute(f"SELECT * FROM [{table_name}]")
        columns = [column[0] for column in self.access_cursor.description]

        column_types = []
        for column in self.access_cursor.description:
            sql_type = self.map_access_type_to_mysql(column[1])
            column_types.append(f"`{column[0]}` {sql_type}")

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            {', '.join(column_types)}
        );
        """
        self.mysql_cursor.execute(create_table_query)
        self.mysql_conn.commit()
        print(f"Tabella `{table_name}` creata in MySQL.")

    def map_access_type_to_mysql(self, access_type):
        """
        Mappa i tipi di dati di Access ai tipi di dati di MySQL.
        """
        if "VARCHAR" in access_type.upper() or "CHAR" in access_type.upper():
            return "VARCHAR(255)"
        elif "INT" in access_type.upper():
            return "INT"
        elif "FLOAT" in access_type.upper() or "DOUBLE" in access_type.upper():
            return "FLOAT"
        elif "DATE" in access_type.upper():
            return "DATE"
        else:
            return "TEXT"

    def transfer_data(self, table_name):
        """
        Trasferisce i dati da una tabella Access a MySQL.
        """
        self.access_cursor.execute(f"SELECT * FROM [{table_name}]")
        rows = self.access_cursor.fetchall()
        columns = [column[0] for column in self.access_cursor.description]
        placeholders = ", ".join(["%s"] * len(columns))

        insert_query = f"""
        INSERT INTO `{table_name}` ({', '.join(columns)})
        VALUES ({placeholders})
        """
        data = [tuple(row) for row in rows]
        try:
            self.mysql_cursor.executemany(insert_query, data)
            self.mysql_conn.commit()
            print(f"Dati trasferiti per la tabella `{table_name}`.")
        except mysql.connector.Error as err:
            print(f"Errore durante il trasferimento dei dati: {err}")
            self.mysql_conn.rollback()
            raise

    def transfer_all_tables(self):
        """
        Trova tutte le tabelle in Access e le trasferisce in MySQL.
        """
        tables = [row.table_name for row in self.access_cursor.tables() if row.table_type == "TABLE"]
        for table in tables:
            try:
                self.create_table_from_access(table)
                self.transfer_data(table)
            except Exception as e:
                print(f"Errore nel trasferimento della tabella `{table}`: {e}")

    def close_connections(self):
        """
        Chiude le connessioni ai database.
        """
        try:
            self.access_cursor.close()
            self.access_conn.close()
            self.mysql_cursor.close()
            self.mysql_conn.close()
            print("Connessioni ai database chiuse.")
        except pyodbc.Error as err:
            print(f"Errore durante la chiusura delle connessioni: {err}")