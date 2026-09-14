from functools import wraps
from flask import request, jsonify

from managers.user_manager import UserManager
from jwt_manager import JWT_Manager

user_manager = UserManager()
jwt_manager = JWT_Manager(
    private_key_path="keys/private_key.pem",
    public_key_path="keys/public_key.pem"
)


def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify({"error": "Missing Authorization header"}), 401

        token = token.replace("Bearer ", "")
        decoded = jwt_manager.decode(token)

        if decoded is None:
            return jsonify({"error": "Invalid or expired token"}), 401

        user = user_manager.get_user_by_id(decoded["id"])
        if user is None:
            return jsonify({"error": "User not found"}), 404

        request.current_user = user
        return f(*args, **kwargs)

    return wrapper


def require_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify({"error": "Missing Authorization header"}), 401

        token = token.replace("Bearer ", "")
        decoded = jwt_manager.decode(token)

        if decoded is None:
            return jsonify({"error": "Invalid or expired token"}), 401

        user = user_manager.get_user_by_id(decoded["id"])
        if user is None:
            return jsonify({"error": "User not found"}), 404

        if user.role != "admin":
            return jsonify({"error": "Admin access required"}), 403

        request.current_user = user
        return f(*args, **kwargs)

    return wrapper