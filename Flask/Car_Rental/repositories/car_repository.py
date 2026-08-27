def create_cars_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lyfter_car_rental.cars (
            id SERIAL PRIMARY KEY,
            brand VARCHAR(50) NOT NULL,
            model VARCHAR(50) NOT NULL,
            year INTEGER NOT NULL,
            status VARCHAR(20) NOT NULL DEFAULT 'available'
        );
    """)


def insert_cars(cursor, cars):
    cursor.executemany("""
        INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
        VALUES (%s, %s, %s, %s);
    """, cars)


def insert_single_car(cursor, brand, model, year, status="available"):
    cursor.execute("""
        INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (brand, model, year, status))
    return cursor.fetchone()[0]


def update_car_status(cursor, car_id, new_status):
    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = %s
        WHERE id = %s
        RETURNING id;
    """, (new_status, car_id))
    return cursor.fetchone()


def get_cars_by_status(cursor, status):
    cursor.execute("""
        SELECT id, brand, model, year, status
        FROM lyfter_car_rental.cars
        WHERE status = %s;
    """, (status,))
    return cursor.fetchall()


ALLOWED_CAR_FILTERS = ['id', 'brand', 'model', 'year', 'status']

def get_cars(cursor, filters=None):
    query = "SELECT id, brand, model, year, status FROM lyfter_car_rental.cars"
    values = []

    if filters:
        valid_filters = {k: v for k, v in filters.items() if k in ALLOWED_CAR_FILTERS}
        if valid_filters:
            conditions = [f"{column} = %s" for column in valid_filters]
            query += " WHERE " + " AND ".join(conditions)
            values = list(valid_filters.values())

    cursor.execute(query, values)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    return [dict(zip(columns, row)) for row in rows]


def get_car_by_id(cursor, car_id):
    cursor.execute("""
        SELECT id, brand, model, year, status
        FROM lyfter_car_rental.cars
        WHERE id = %s;
    """, (car_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    columns = [desc[0] for desc in cursor.description]
    return dict(zip(columns, row))