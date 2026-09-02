import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.user_repository import update_user_status

connection = get_connection()
cursor = connection.cursor()

try:
    result = update_user_status(cursor, user_id=1, new_status="suspended")

    if result is None:
        print("No user found with that id.")
    else:
        connection.commit()
        print(f"User {result[0]} status updated successfully.")

finally:
    cursor.close()
    connection.close()