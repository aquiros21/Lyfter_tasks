import sys
import os
import psycopg2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.user_repository import insert_single_user

connection = get_connection()
cursor = connection.cursor()

try:
    new_id = insert_single_user(
        cursor,
        full_name="Test User",
        email="test.user@email.com",
        username="testuser1",
        password="mypassword",
        birth_date="1995-03-20",
        status="active"
    )
    connection.commit()
    print(f"User created with id: {new_id}")

except psycopg2.errors.UniqueViolation:
    connection.rollback()
    print("Error: A user with this email or username already exists.")

finally:
    cursor.close()
    connection.close()