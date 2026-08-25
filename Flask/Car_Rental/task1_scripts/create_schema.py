import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;")
connection.commit()

print("Schema 'lyfter_car_rental' created successfully!")

cursor.close()
connection.close()