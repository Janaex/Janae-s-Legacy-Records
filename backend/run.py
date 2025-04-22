from app import create_app
import mysql.connector
from app.config import DATABASE

def create_connection():
    connection = mysql.connector.connect(
        user=DATABASE['root'],
        password=DATABASE['kristopher'],
        host=DATABASE['localhost'],
        database=DATABASE['record']
    )
    return connection

app = create_app()

if __name__ == '__main__':
    app.run()