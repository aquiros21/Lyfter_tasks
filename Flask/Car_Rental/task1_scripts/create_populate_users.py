import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_config import get_connection
from repositories.user_repository import create_users_table, insert_users

FIRST_NAMES = [
    "Maria", "Carlos", "Ana", "Luis", "Sofia", "Jorge", "Laura", "Diego",
    "Valentina", "Andres", "Camila", "Miguel", "Paula", "Ricardo", "Daniela",
    "Fernando", "Gabriela", "Javier", "Isabella", "Manuel"
]

LAST_NAMES = [
    "Gomez", "Ruiz", "Martinez", "Lopez", "Hernandez", "Gonzalez", "Perez",
    "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Diaz", "Castro",
    "Ortiz", "Morales", "Vargas", "Jimenez", "Rojas", "Mendoza"
]

def generate_users(count=50):
    users = []
    used_usernames = set()

    for i in range(count):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        full_name = f"{first} {last}"

        username = f"{first.lower()}.{last.lower()}{i}"
        used_usernames.add(username)

        email = f"{username}@email.com"
        password = f"pass{1000 + i}"

        year = random.randint(1970, 2005)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birth_date = f"{year}-{month:02d}-{day:02d}"

        status = "active"

        users.append((full_name, email, username, password, birth_date, status))

    return users


connection = get_connection()
cursor = connection.cursor()

create_users_table(cursor)

users = generate_users(50)
insert_users(cursor, users)

connection.commit()

print(f"Created table and inserted {len(users)} users successfully!")

cursor.close()
connection.close()