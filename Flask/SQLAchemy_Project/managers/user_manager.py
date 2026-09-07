from sqlalchemy.orm import joinedload

from db_config import get_session
from models import User


class UserManager:

    def create_user(self, full_name, email, username, password, birth_date, status="active"):
        session = get_session()
        try:
            new_user = User(
                full_name=full_name,
                email=email,
                username=username,
                password=password,
                birth_date=birth_date,
                status=status
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user.id
        finally:
            session.close()

    def update_user(self, user_id, **fields):
        session = get_session()
        try:
            user = session.get(User, user_id)
            if user is None:
                return None

            valid_columns = {column.name for column in User.__table__.columns}

            for key, value in fields.items():
                if key not in valid_columns:
                    raise ValueError(f"'{key}' is not a valid column on User")
                setattr(user, key, value)

            session.commit()
            return user.id
        finally:
            session.close()

    def delete_user(self, user_id):
        session = get_session()
        try:
            user = session.get(User, user_id)
            if user is None:
                return False

            session.delete(user)
            session.commit()
            return True
        finally:
            session.close()

    def get_all_users(self):
        session = get_session()
        try:
            return session.query(User).options(
                joinedload(User.addresses),
                joinedload(User.cars)
            ).all()
        finally:
            session.close()