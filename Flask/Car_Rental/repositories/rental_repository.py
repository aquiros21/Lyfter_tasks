def create_rentals_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lyfter_car_rental.rentals (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES lyfter_car_rental.users(id),
            car_id INTEGER NOT NULL REFERENCES lyfter_car_rental.cars(id),
            rental_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(20) NOT NULL DEFAULT 'active'
        );
    """)


def create_rental(cursor, user_id, car_id):
    cursor.execute("""
        INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
        VALUES (%s, %s, 'active')
        RETURNING id;
    """, (user_id, car_id))
    return cursor.fetchone()[0]


def complete_rental(cursor, rental_id):
    cursor.execute("""
        UPDATE lyfter_car_rental.rentals
        SET status = 'completed'
        WHERE id = %s
        RETURNING id, car_id;
    """, (rental_id,))
    return cursor.fetchone()


def update_rental_status(cursor, rental_id, new_status):
    cursor.execute("""
        UPDATE lyfter_car_rental.rentals
        SET status = %s
        WHERE id = %s
        RETURNING id;
    """, (new_status, rental_id))
    return cursor.fetchone()


ALLOWED_RENTAL_FILTERS = ['id', 'user_id', 'car_id', 'status']

def get_rentals(cursor, filters=None):
    query = "SELECT id, user_id, car_id, rental_date, status FROM lyfter_car_rental.rentals"
    values = []

    if filters:
        valid_filters = {k: v for k, v in filters.items() if k in ALLOWED_RENTAL_FILTERS}
        if valid_filters:
            conditions = [f"{column} = %s" for column in valid_filters]
            query += " WHERE " + " AND ".join(conditions)
            values = list(valid_filters.values())

    cursor.execute(query, values)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    return [dict(zip(columns, row)) for row in rows]