from db_config import get_session
from models import Address


class AddressManager:

    def create_address(self, user_id, street, city, country, zip_code):
        session = get_session()
        try:
            new_address = Address(
                user_id=user_id,
                street=street,
                city=city,
                country=country,
                zip_code=zip_code
            )
            session.add(new_address)
            session.commit()
            session.refresh(new_address)
            return new_address.id
        finally:
            session.close()

    def update_address(self, address_id, **fields):
        session = get_session()
        try:
            address = session.get(Address, address_id)
            if address is None:
                return None

            for key, value in fields.items():
                setattr(address, key, value)

            session.commit()
            return address.id
        finally:
            session.close()

    def delete_address(self, address_id):
        session = get_session()
        try:
            address = session.get(Address, address_id)
            if address is None:
                return False

            session.delete(address)
            session.commit()
            return True
        finally:
            session.close()

    def get_all_addresses(self):
        session = get_session()
        try:
            return session.query(Address).all()
        finally:
            session.close()