import pyodbc

def read_access(file_path):
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={file_path};"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TableName")
    return [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
