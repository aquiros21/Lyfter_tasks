from db_config import get_session
from models import Invoice, Product


class InvoiceManager:

    def create_purchase(self, user_id, product_id, quantity):
        session = get_session()
        try:
            if not isinstance(quantity, int) or quantity <= 0:
                return {"error": "invalid_quantity"}

            product = session.get(Product, product_id)

            if product is None:
                return {"error": "not_found"}

            if product.quantity < quantity:
                return {"error": "insufficient_stock"}

            total_price = product.price * quantity

            new_invoice = Invoice(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
                total_price=total_price
            )
            session.add(new_invoice)

            product.quantity -= quantity

            session.commit()
            session.refresh(new_invoice)
            return new_invoice

        finally:
            session.close()

    def get_invoices_by_user(self, user_id):
        session = get_session()
        try:
            return session.query(Invoice).filter_by(user_id=user_id).all()
        finally:
            session.close()