from flask import Blueprint, request, jsonify
from repositories.user_repository import insert_single_user, update_user_status
import psycopg2
from repositories.user_repository import insert_single_user, update_user_status, get_users
from db_config import get_connection
from repositories.user_repository import insert_single_user

user_bp = Blueprint('user_routes', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    required_fields = ['full_name', 'email', 'username', 'password', 'birth_date']
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing {field}"}), 400

    connection = get_connection()
    cursor = connection.cursor()

    try:
        new_id = insert_single_user(
            cursor,
            full_name=data['full_name'],
            email=data['email'],
            username=data['username'],
            password=data['password'],
            birth_date=data['birth_date'],
            status=data.get('status', 'active')
        )
        connection.commit()
        return jsonify({"id": new_id, "message": "User created successfully"}), 201

    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        return jsonify({"error": "A user with this email or username already exists"}), 400

    finally:
        cursor.close()
        connection.close()


@user_bp.route('/users/<int:user_id>/status', methods=['PATCH'])
def change_user_status(user_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not data.get('status'):
        return jsonify({"error": "Missing status"}), 400

    connection = get_connection()
    cursor = connection.cursor()

    try:
        result = update_user_status(cursor, user_id, data['status'])

        if result is None:
            return jsonify({"error": "User not found"}), 404

        connection.commit()
        return jsonify({"id": result[0], "message": "User status updated"}), 200

    finally:
        cursor.close()
        connection.close()


@user_bp.route('/users/<int:user_id>/flag-delinquent', methods=['PATCH'])
def flag_user_delinquent(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        result = update_user_status(cursor, user_id, "delinquent")

        if result is None:
            return jsonify({"error": "User not found"}), 404

        connection.commit()
        return jsonify({"id": result[0], "message": "User flagged as delinquent"}), 200

    finally:
        cursor.close()
        connection.close()


@user_bp.route('/users', methods=['GET'])
def list_users():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        filters = request.args.to_dict()
        users = get_users(cursor, filters)
        return jsonify(users), 200

    finally:
        cursor.close()
        connection.close()