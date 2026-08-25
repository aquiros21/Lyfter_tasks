import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.car_repository import update_car_status

connection = get_connection()
cursor = connection.cursor()

try:
    car_id = 5
    result = update_car_status(cursor, car_id, "disabled")

    if result is None:
        print("No car found with that id.")
    else:
        connection.commit()
        print(f"Car {result[0]} has been disabled.")

finally:
    cursor.close()
    connection.close()