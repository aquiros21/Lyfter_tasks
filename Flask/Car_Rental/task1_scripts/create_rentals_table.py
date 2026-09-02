import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.rental_repository import create_rentals_table

connection = get_connection()
cursor = connection.cursor()

create_rentals_table(cursor)
connection.commit()

print("Rentals table created successfully!")

cursor.close()
connection.close()