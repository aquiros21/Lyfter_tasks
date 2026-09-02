import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.rental_repository import complete_rental
from repositories.car_repository import update_car_status

connection = get_connection()
cursor = connection.cursor()

try:
    rental_id = 1

    result = complete_rental(cursor, rental_id)

    if result is None:
        print("No rental found with that id.")
    else:
        completed_rental_id, car_id = result
        update_car_status(cursor, car_id, "available")
        connection.commit()
        print(f"Rental {completed_rental_id} completed, car {car_id} marked as available.")

finally:
    cursor.close()
    connection.close()