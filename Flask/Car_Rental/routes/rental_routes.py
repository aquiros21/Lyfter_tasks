from flask import Blueprint, request, jsonify
import psycopg2
from repositories.rental_repository import create_rental, complete_rental, update_rental_status
from db_config import get_connection
from repositories.rental_repository import create_rental
from repositories.car_repository import update_car_status
from repositories.rental_repository import create_rental, complete_rental, update_rental_status, get_rentals


rental_bp = Blueprint('rental_routes', __name__)


@rental_bp.route('/rentals', methods=['POST'])
def create_rental_route():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    required_fields = ['user_id', 'car_id']
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing {field}"}), 400

    connection = get_connection()
    cursor = connection.cursor()

    try:
        rental_id = create_rental(cursor, data['user_id'], data['car_id'])
        update_car_status(cursor, data['car_id'], "rented")
        connection.commit()
        return jsonify({"id": rental_id, "message": "Rental created successfully"}), 201

    except psycopg2.errors.ForeignKeyViolation:
        connection.rollback()
        return jsonify({"error": "Invalid user_id or car_id"}), 400

    finally:
        cursor.close()
        connection.close()


@rental_bp.route('/rentals/<int:rental_id>/complete', methods=['PATCH'])
def complete_rental_route(rental_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        result = complete_rental(cursor, rental_id)

        if result is None:
            return jsonify({"error": "Rental not found"}), 404

        completed_rental_id, car_id = result
        update_car_status(cursor, car_id, "available")
        connection.commit()

        return jsonify({"id": completed_rental_id, "message": "Rental completed, car marked as available"}), 200

    finally:
        cursor.close()
        connection.close()


@rental_bp.route('/rentals/<int:rental_id>/status', methods=['PATCH'])
def change_rental_status(rental_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not data.get('status'):
        return jsonify({"error": "Missing status"}), 400

    connection = get_connection()
    cursor = connection.cursor()

    try:
        result = update_rental_status(cursor, rental_id, data['status'])

        if result is None:
            return jsonify({"error": "Rental not found"}), 404

        connection.commit()
        return jsonify({"id": result[0], "message": "Rental status updated"}), 200

    finally:
        cursor.close()
        connection.close()


@rental_bp.route('/rentals', methods=['GET'])
def list_rentals():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        filters = request.args.to_dict()
        rentals = get_rentals(cursor, filters)
        return jsonify(rentals), 200

    finally:
        cursor.close()
        connection.close()