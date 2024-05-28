from api.models.product import Product
from api.models.inventory import Inventory
from api.models.order import Order
from api.models.order_item import OrderItem

import datetime



def test_new_product():
    product = Product('X',1.0,2.0)
    
    print(product.sku)
    assert isinstance(product.name, str)
    assert isinstance(product.cost, float)
    assert isinstance(product.price, float)


def test_new_product_inventory():
    product = Product('X',1.0,2.0)
    product_inventory = Inventory(product.id)

    assert product_inventory.stock == 100


def test_new_order():
    order = Order()
    assert isinstance(order.created_date,datetime.datetime)


def test_new_order_items():
    product1 = Product('X1',1.0,2.0)
    product2= Product('X2',1.0,2.0)
    product3 = Product('X3',1.0,2.0)
    product4 = Product('X4',1.0,2.0)

    order = Order()
    assert isinstance(order.created_date,datetime.datetime)

    order_item1=OrderItem(
        order.id,
        datetime.datetime.now,
        {
            "product_id":product1.id,
            "quantity":1
         })
    order_item2=OrderItem(
        order.id,
        datetime.datetime.now,
        {
            "product_id":product2.id,
            "quantity":1
         })
    order_item3=OrderItem(
        order.id,
        datetime.datetime.now,
        {
            "product_id":product3.id,
            "quantity":4
         })
    order_item4=OrderItem(
        order.id,
        datetime.datetime.now,
        {
            "product_id":product4.id,
            "quantity":3
         })
    assert order_item1.order_id == order.id
    assert order_item2.order_id == order.id
    assert order_item3.order_id == order.id
    assert order_item4.order_id == order.id