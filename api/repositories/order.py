from api.database import db
from api.models.order import Order
from api.models.order_item import OrderItem
from api.models.inventory import Inventory

class OrderRepository:
    @staticmethod
    def set_order(request_json) -> dict:
        order = Order()
        order.save()
        for item in request_json['order_items']:
            item = OrderItem(order.id,order.created_date,item)
            item.save()
            item_inventory = Inventory.query.filter_by(product_id=item.product_id).first()
            item_inventory.add_stock(-item.quantity)
            item_inventory.save()

        return order
