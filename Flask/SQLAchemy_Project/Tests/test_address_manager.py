import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from managers.user_manager import UserManager
from managers.address_manager import AddressManager

user_manager = UserManager()
address_manager = AddressManager()

user_id = user_manager.create_user(
    full_name="Address Owner",
    email="address.owner@email.com",
    username="addressowner1",
    password="mypassword",
    birth_date="1992-06-15"
)
print(f"Created user with id: {user_id}")

address_id = address_manager.create_address(
    user_id=user_id,
    street="123 Main St",
    city="San Jose",
    country="Costa Rica",
    zip_code="10101"
)
print(f"Created address with id: {address_id}")

updated_id = address_manager.update_address(address_id, city="Heredia")
print(f"Updated address, id: {updated_id}")

all_addresses = address_manager.get_all_addresses()
print(f"\nTotal addresses: {len(all_addresses)}")
for address in all_addresses:
    print(address.id, address.street, address.city, "user:", address.user_id)

deleted = address_manager.delete_address(address_id)
print(f"\nDeleted address? {deleted}")