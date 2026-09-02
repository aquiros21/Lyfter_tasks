import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.car_repository import create_cars_table, insert_cars

BRANDS_MODELS = [
    ("Toyota", "Corolla"),
    ("Toyota", "RAV4"),
    ("Honda", "Civic"),
    ("Honda", "CR-V"),
    ("Ford", "Focus"),
    ("Ford", "Escape"),
    ("Chevrolet", "Spark"),
    ("Chevrolet", "Onix"),
    ("Nissan", "Sentra"),
    ("Nissan", "Kicks"),
    ("Hyundai", "Accent"),
    ("Hyundai", "Tucson"),
    ("Kia", "Rio"),
    ("Kia", "Sportage"),
    ("Mazda", "3"),
]

def generate_cars(count=50):
    cars = []

    for i in range(count):
        brand, model = random.choice(BRANDS_MODELS)
        year = random.randint(2015, 2024)
        status = "available"

        cars.append((brand, model, year, status))

    return cars


connection = get_connection()
cursor = connection.cursor()

create_cars_table(cursor)

cars = generate_cars(50)
insert_cars(cursor, cars)

connection.commit()

print(f"Created table and inserted {len(cars)} cars successfully!")

cursor.close()
connection.close()