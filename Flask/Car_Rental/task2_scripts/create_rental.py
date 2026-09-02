import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.rental_repository import create_rental
from repositories.car_repository import update_car_status

connection = get_connection()
cursor = connection.cursor()

try:
    user_id = 2
    car_id = 3

    rental_id = create_rental(cursor, user_id, car_id)
    update_car_status(cursor, car_id, "rented")

    connection.commit()
    print(f"Rental created with id: {rental_id}, car {car_id} marked as rented.")

finally:
    cursor.close()
    connection.close()