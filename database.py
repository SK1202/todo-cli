import mysql.connector


def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SK@MySQL1202",
            database="todo_db"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None