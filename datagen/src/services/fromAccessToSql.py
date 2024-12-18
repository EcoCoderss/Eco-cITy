import pyodbc
import pymysql
from pymysql.constants import CLIENT

# Configurazione del database Access
ACCESS_DB_PATH = "C:\Users\garrighini\Downloads\Database11.accdb"
ACCESS_DRIVER = "Microsoft Access Driver (*.mdb, *.accdb)"
access_conn_str = f"DRIVER={{{ACCESS_DRIVER}}};DBQ={ACCESS_DB_PATH};"

# Configurazione del database MySQL
MYSQL_HOST = "localhost"
MYSQL_USER = "your_mysql_user"
MYSQL_PASSWORD = "your_mysql_password"
MYSQL_DB = "your_mysql_db"

# Parametri per ottimizzare le operazioni
BATCH_SIZE = 1000  # Numero di righe per batch di inserimento

# Funzione per ottenere i tipi di colonna da Access
def map_access_types_to_mysql(access_type):
    mapping = {
        "int": "INT",
        "float": "FLOAT",
        "double": "DOUBLE",
        "decimal": "DECIMAL(10,2)",
        "datetime": "DATETIME",
        "date": "DATE",
        "text": "TEXT",
        "longchar": "TEXT",
        "yesno": "BOOLEAN",
    }
    return mapping.get(access_type, "TEXT")

def copy_access_to_mysql():
    try:
        # Connessione al database MySQL
        mysql_conn = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            client_flag=CLIENT.MULTI_STATEMENTS
        )
        mysql_cursor = mysql_conn.cursor()

        # Connessione al database Access
        access_conn = pyodbc.connect(access_conn_str)
        access_cursor = access_conn.cursor()

        # Recupera le tabelle di Access
        access_cursor.execute("SELECT Name FROM MSysObjects WHERE Type=1 AND Flags=0")
        tables = [row[0] for row in access_cursor.fetchall()]

        for table in tables:
            print(f"Trasferimento tabella: {table}")

            # Recupera le colonne della tabella
            access_cursor.execute(f"SELECT TOP 1 * FROM {table}")
            columns = [column[0] for column in access_cursor.description]
            col_defs = ", ".join([f"`{col}` TEXT" for col in columns])  # Ottimizzare i tipi dinamici se necessario

            # Crea la tabella MySQL
            mysql_cursor.execute(f"DROP TABLE IF EXISTS `{table}`;")
            mysql_cursor.execute(f"CREATE TABLE `{table}` ({col_defs});")

            # Recupera e inserisce i dati in batch
            access_cursor.execute(f"SELECT * FROM {table}")
            while True:
                rows = access_cursor.fetchmany(BATCH_SIZE)  # Leggi un batch di righe
                if not rows:
                    break
                placeholders = ", ".join(["%s"] * len(columns))
                mysql_cursor.executemany(
                    f"INSERT INTO `{table}` ({', '.join(columns)}) VALUES ({placeholders})", rows
                )
                mysql_conn.commit()
                print(f"Inserite {len(rows)} righe nella tabella {table}")

            print(f"Tabella {table} trasferita con successo!")

        print("Tutte le tabelle sono state trasferite correttamente.")

    except Exception as e:
        print(f"Errore durante la migrazione: {e}")

    finally:
        # Chiude le connessioni
        access_cursor.close()
        access_conn.close()
        mysql_cursor.close()
        mysql_conn.close()

if __name__ == "__main__":
    copy_access_to_mysql()
