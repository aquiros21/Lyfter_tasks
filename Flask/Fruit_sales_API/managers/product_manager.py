from db_config import get_session
from models import Product


class ProductManager:

    EDITABLE_COLUMNS = {"name", "price", "entry_date", "quantity"}

    def create_product(self, name, price, entry_date, quantity):
        session = get_session()
        try:
            new_product = Product(
                name=name,
                price=price,
                entry_date=entry_date,
                quantity=quantity
            )
            session.add(new_product)
            session.commit()
            session.refresh(new_product)
            return new_product
        finally:
            session.close()

    def get_all_products(self):
        session = get_session()
        try:
            return session.query(Product).all()
        finally:
            session.close()

    def get_product_by_id(self, product_id):
        session = get_session()
        try:
            return session.query(Product).filter_by(id=product_id).first()
        finally:
            session.close()

    def update_product(self, product_id, **fields):
        session = get_session()
        try:
            product = session.get(Product, product_id)
            if product is None:
                return None

            for key, value in fields.items():
                if key not in self.EDITABLE_COLUMNS:
                    raise ValueError(f"'{key}' is not an editable field on Product")
                setattr(product, key, value)

            session.commit()
            session.refresh(product)
            return product
        finally:
            session.close()

    def delete_product(self, product_id):
        session = get_session()
        try:
            product = session.get(Product, product_id)
            if product is None:
                return False

            session.delete(product)
            session.commit()
            return True
        finally:
            session.close()