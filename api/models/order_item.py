
from api.database import db
from api.models.order import Order
from api.models.product import Product
from api.models.base_model import BaseModel
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKeyConstraint


class OrderItem(BaseModel, db.Model):
    __tablename__ = 'order_item'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)

    __table_args__ = (        
        ForeignKeyConstraint([order_id], [Order.id], ondelete='NO ACTION'),
        ForeignKeyConstraint([product_id], [Product.id], ondelete='NO ACTION'),      
    )

    def __init__(self,order_id,date,item):
        self.order_id = order_id
        self.created_date = date
        self.product_id =  item["product_id"]
        self.quantity = item["quantity"]

