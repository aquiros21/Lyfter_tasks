import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.car_repository import get_cars_by_status

connection = get_connection()
cursor = connection.cursor()

try:
    rented_cars = get_cars_by_status(cursor, "rented")
    print(f"\nRented cars ({len(rented_cars)}):")
    for car in rented_cars:
        print(car)

    available_cars = get_cars_by_status(cursor, "available")
    print(f"\nAvailable cars ({len(available_cars)}):")
    for car in available_cars:
        print(car)

    disabled_cars = get_cars_by_status(cursor, "disabled")
    print(f"\nDisabled cars ({len(disabled_cars)}):")
    for car in disabled_cars:
        print(car)

finally:
    cursor.close()
    connection.close()