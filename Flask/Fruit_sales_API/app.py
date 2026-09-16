from flask import Flask, request, jsonify
from sqlalchemy.exc import IntegrityError

from db_config import engine
from models import Base
from managers.user_manager import UserManager
from managers.product_manager import ProductManager
from managers.invoice_manager import InvoiceManager
from jwt_manager import JWT_Manager
from auth_decorators import require_auth, require_admin

Base.metadata.create_all(engine)

app = Flask("user-service")

user_manager = UserManager()
product_manager = ProductManager()
invoice_manager = InvoiceManager()
jwt_manager = JWT_Manager(
    private_key_path="keys/private_key.pem",
    public_key_path="keys/public_key.pem"
)


@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing username or password"}), 400

    try:
        new_user = user_manager.create_user(data["username"], data["password"])
        token = jwt_manager.encode({"id": new_user.id})
        return jsonify(token=token), 201

    except IntegrityError:
        return jsonify({"error": "Username already exists"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing username or password"}), 400

    user = user_manager.get_user_by_credentials(data["username"], data["password"])

    if user is None:
        return jsonify({"error": "Invalid username or password"}), 401

    token = jwt_manager.encode({"id": user.id})
    return jsonify(token=token), 200


@app.route("/me")
@require_auth
def me():
    user = request.current_user
    return jsonify(id=user.id, username=user.username, role=user.role), 200


@app.route("/products", methods=["POST"])
@require_admin
def create_product():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    required_fields = ["name", "price", "entry_date", "quantity"]
    for field in required_fields:
        if data.get(field) is None:
            return jsonify({"error": f"Missing {field}"}), 400

    new_product = product_manager.create_product(
        name=data["name"],
        price=data["price"],
        entry_date=data["entry_date"],
        quantity=data["quantity"]
    )

    return jsonify({
        "id": new_product.id,
        "name": new_product.name,
        "price": str(new_product.price),
        "entry_date": str(new_product.entry_date),
        "quantity": new_product.quantity
    }), 201


@app.route("/products", methods=["GET"])
@require_admin
def list_products():
    products = product_manager.get_all_products()
    result = [
        {
            "id": p.id,
            "name": p.name,
            "price": str(p.price),
            "entry_date": str(p.entry_date),
            "quantity": p.quantity
        }
        for p in products
    ]
    return jsonify(result), 200


@app.route("/products/<int:product_id>", methods=["PUT"])
@require_admin
def update_product_route(product_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    try:
        updated = product_manager.update_product(product_id, **data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    if updated is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "id": updated.id,
        "name": updated.name,
        "price": str(updated.price),
        "entry_date": str(updated.entry_date),
        "quantity": updated.quantity
    }), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
@require_admin
def delete_product_route(product_id):
    deleted = product_manager.delete_product(product_id)

    if not deleted:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({"message": "Product deleted"}), 200


@app.route("/purchase", methods=["POST"])
@require_auth
def purchase():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    if data.get("product_id") is None or data.get("quantity") is None:
        return jsonify({"error": "Missing product_id or quantity"}), 400

    user = request.current_user

    result = invoice_manager.create_purchase(
        user_id=user.id,
        product_id=data["product_id"],
        quantity=data["quantity"]
    )

    if isinstance(result, dict):
        if result.get("error") == "invalid_quantity":
            return jsonify({"error": "Quantity must be a positive integer"}), 400
        if result.get("error") == "not_found":
            return jsonify({"error": "Product not found"}), 404
        if result.get("error") == "insufficient_stock":
            return jsonify({"error": "Not enough stock available"}), 400

    return jsonify({
        "id": result.id,
        "product_id": result.product_id,
        "quantity": result.quantity,
        "total_price": str(result.total_price),
        "purchase_date": str(result.purchase_date)
    }), 201


@app.route("/invoices", methods=["GET"])
@require_auth
def list_invoices():
    user = request.current_user
    invoices = invoice_manager.get_invoices_by_user(user.id)

    result = [
        {
            "id": inv.id,
            "product_id": inv.product_id,
            "quantity": inv.quantity,
            "total_price": str(inv.total_price),
            "purchase_date": str(inv.purchase_date)
        }
        for inv in invoices
    ]
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)