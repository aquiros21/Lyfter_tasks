from flask import Blueprint, request, jsonify
from repositories.car_repository import insert_single_car, update_car_status
from db_config import get_connection
from repositories.car_repository import insert_single_car
from repositories.car_repository import insert_single_car, update_car_status, get_cars

car_bp = Blueprint('car_routes', __name__)


@car_bp.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    required_fields = ['brand', 'model', 'year']
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing {field}"}), 400

    connection = get_connection()
    cursor = connection.cursor()

    try:
        new_id = insert_single_car(
            cursor,
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            status=data.get('status', 'available')
        )
        connection.commit()
        return jsonify({"id": new_id, "message": "Car created successfully"}), 201

    finally:
        cursor.close()
        connection.close()


@car_bp.route('/cars/<int:car_id>/status', methods=['PATCH'])
def change_car_status(car_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not data.get('status'):
        return jsonify({"error": "Missing status"}), 400

    connection = get_connection()
    cursor = connection.cursor()

    try:
        result = update_car_status(cursor, car_id, data['status'])

        if result is None:
            return jsonify({"error": "Car not found"}), 404

        connection.commit()
        return jsonify({"id": result[0], "message": "Car status updated"}), 200

    finally:
        cursor.close()
        connection.close()


@car_bp.route('/cars', methods=['GET'])
def list_cars():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        filters = request.args.to_dict()
        cars = get_cars(cursor, filters)
        return jsonify(cars), 200

    finally:
        cursor.close()
        connection.close()