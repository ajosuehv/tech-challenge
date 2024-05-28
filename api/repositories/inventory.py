from api.models.product import Product
from api.models.inventory import Inventory

class InventoryRepository:
    @staticmethod
    def add_inventory(product_id,body):
        inventory = Inventory.query.filter_by(product_id=product_id).first()
        inventory.add_stock(body["quantity"])
        inventory.save()
        return inventory
