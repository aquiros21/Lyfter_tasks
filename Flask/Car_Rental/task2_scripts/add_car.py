import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.car_repository import insert_single_car

connection = get_connection()
cursor = connection.cursor()

try:
    new_id = insert_single_car(
        cursor,
        brand="Toyota",
        model="Camry",
        year=2023,
        status="available"
    )
    connection.commit()
    print(f"Car created with id: {new_id}")

finally:
    cursor.close()
    connection.close()