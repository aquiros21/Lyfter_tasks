def create_users_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lyfter_car_rental.users (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(70) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            birth_date DATE NOT NULL,
            status VARCHAR(20) NOT NULL DEFAULT 'active'
        );
    """)


def insert_users(cursor, users):
    cursor.executemany("""
        INSERT INTO lyfter_car_rental.users (full_name, email, username, password, birth_date, status)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, users)


def insert_single_user(cursor, full_name, email, username, password, birth_date, status="active"):
    cursor.execute("""
        INSERT INTO lyfter_car_rental.users (full_name, email, username, password, birth_date, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id;
    """, (full_name, email, username, password, birth_date, status))
    return cursor.fetchone()[0]


def update_user_status(cursor, user_id, new_status):
    cursor.execute("""
        UPDATE lyfter_car_rental.users
        SET status = %s
        WHERE id = %s
        RETURNING id;
    """, (new_status, user_id))
    return cursor.fetchone()


ALLOWED_USER_FILTERS = ['id', 'full_name', 'email', 'username', 'status']

def get_users(cursor, filters=None):
    query = "SELECT id, full_name, email, username, birth_date, status FROM lyfter_car_rental.users"
    values = []

    if filters:
        valid_filters = {k: v for k, v in filters.items() if k in ALLOWED_USER_FILTERS}
        if valid_filters:
            conditions = [f"{column} = %s" for column in valid_filters]
            query += " WHERE " + " AND ".join(conditions)
            values = list(valid_filters.values())

    cursor.execute(query, values)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    return [dict(zip(columns, row)) for row in rows]


def get_user_by_id(cursor, user_id):
    cursor.execute("""
        SELECT id, full_name, email, username, status
        FROM lyfter_car_rental.users
        WHERE id = %s;
    """, (user_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    columns = [desc[0] for desc in cursor.description]
    return dict(zip(columns, row))