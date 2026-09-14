from db_config import get_session
from models import User


class UserManager:

    def create_user(self, username, password, role="user"):
        session = get_session()
        try:
            new_user = User(username=username, password=password, role=role)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
        finally:
            session.close()

    def get_user_by_credentials(self, username, password):
        session = get_session()
        try:
            return session.query(User).filter_by(username=username, password=password).first()
        finally:
            session.close()

    def get_user_by_id(self, user_id):
        session = get_session()
        try:
            return session.query(User).filter_by(id=user_id).first()
        finally:
            session.close()