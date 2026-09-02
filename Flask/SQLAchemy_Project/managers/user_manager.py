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

            for key, value in fields.items():
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
            return session.query(User).all()
        finally:
            session.close()