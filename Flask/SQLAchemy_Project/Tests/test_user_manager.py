import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from managers.user_manager import UserManager

manager = UserManager()

new_id = manager.create_user(
    full_name="Test Manager",
    email="test.manager@email.com",
    username="testmanager1",
    password="mypassword",
    birth_date="1997-04-10"
)
print(f"Created user with id: {new_id}")

updated_id = manager.update_user(new_id, status="suspended")
print(f"Updated user id: {updated_id}")

all_users = manager.get_all_users()
print(f"\nTotal users: {len(all_users)}")
for user in all_users:
    print(user.id, user.full_name, user.status)

deleted = manager.delete_user(new_id)
print(f"\nDeleted user? {deleted}")

all_users_after = manager.get_all_users()
print(f"Total users after delete: {len(all_users_after)}")