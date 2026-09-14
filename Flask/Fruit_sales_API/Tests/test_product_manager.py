import sys
import os
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from managers.product_manager import ProductManager

manager = ProductManager()

new_product = manager.create_product(
    name="Apple",
    price=1.50,
    entry_date=date.today(),
    quantity=100
)
print(f"Created product with id: {new_product.id}")

updated = manager.update_product(new_product.id, quantity=80)
print(f"Updated quantity to: {updated.quantity}")

all_products = manager.get_all_products()
print(f"\nTotal products: {len(all_products)}")
for p in all_products:
    print(p.id, p.name, p.price, p.quantity)

deleted = manager.delete_product(new_product.id)
print(f"\nDeleted product? {deleted}")