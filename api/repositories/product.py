from api.database import db
from api.models.product import Product
from api.models.inventory import Inventory

class ProductRepository:
    @staticmethod
    def get():
        return {'':''}

    @staticmethod
    def new_product(request_json) -> dict:

        product_name=request_json["name"]
        cost=request_json["cost"]
        price=request_json["price"]
        product = Product(product_name, cost, price)
        product.save()

        product_inventory = Inventory(product.id)
        product_inventory.save()
        
        return product
