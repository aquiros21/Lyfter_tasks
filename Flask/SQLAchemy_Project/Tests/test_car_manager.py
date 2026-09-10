import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from managers.user_manager import UserManager
from managers.car_manager import CarManager

user_manager = UserManager()
car_manager = CarManager()

user_id = user_manager.create_user(
    full_name="Car Owner",
    email="car.owner@email.com",
    username="carowner1",
    password="mypassword",
    birth_date="1990-01-01"
)
print(f"Created user with id: {user_id}")

car_id = car_manager.create_car(brand="Toyota", model="Corolla", year=2022)
print(f"Created unassigned car with id: {car_id}")

assigned_id = car_manager.assign_car_to_user(car_id, user_id)
print(f"Assigned car {assigned_id} to user {user_id}")

updated_id = car_manager.update_car(car_id, status="rented")
print(f"Updated car status, id: {updated_id}")

all_cars = car_manager.get_all_cars()
print(f"\nTotal cars: {len(all_cars)}")
for car in all_cars:
    print(car.id, car.brand, car.model, car.status, "owner:", car.user_id)

deleted = car_manager.delete_car(car_id)
print(f"\nDeleted car? {deleted}")