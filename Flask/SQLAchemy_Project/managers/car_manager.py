from sqlalchemy.orm import joinedload

from db_config import get_session
from models import Car


class CarManager:

    def create_car(self, brand, model, year, status="available", user_id=None):
        session = get_session()
        try:
            new_car = Car(
                brand=brand,
                model=model,
                year=year,
                status=status,
                user_id=user_id
            )
            session.add(new_car)
            session.commit()
            session.refresh(new_car)
            return new_car.id
        finally:
            session.close()

    def update_car(self, car_id, **fields):
        session = get_session()
        try:
            car = session.get(Car, car_id)
            if car is None:
                return None

            valid_columns = {column.name for column in Car.__table__.columns}

            for key, value in fields.items():
                if key not in valid_columns:
                    raise ValueError(f"'{key}' is not a valid column on Car")
                setattr(car, key, value)

            session.commit()
            return car.id
        finally:
            session.close()

    def delete_car(self, car_id):
        session = get_session()
        try:
            car = session.get(Car, car_id)
            if car is None:
                return False

            session.delete(car)
            session.commit()
            return True
        finally:
            session.close()

    def get_all_cars(self):
        session = get_session()
        try:
            return session.query(Car).options(joinedload(Car.user)).all()
        finally:
            session.close()

    def assign_car_to_user(self, car_id, user_id):
        session = get_session()
        try:
            car = session.get(Car, car_id)
            if car is None:
                return None

            car.user_id = user_id
            session.commit()
            return car.id
        finally:
            session.close()