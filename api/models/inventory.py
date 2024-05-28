from api.database import db
from api.models.base_model import BaseModel
from api.models.product import Product
from sqlalchemy import ForeignKeyConstraint
import logging


class Inventory(BaseModel, db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer(), nullable=False)
    stock = db.Column(db.Integer())
    
    __table_args__ = (        
        ForeignKeyConstraint([product_id], [Product.id], ondelete='NO ACTION'),      
    )

    def add_stock(self, new_stock):
        self.stock = self.stock + new_stock
        if self.stock < 10:
            logging.warning("Low stock level for product_id ={product_id},\n {stock}  units left".format(product_id=self.product_id, stock=self.stock))
            

    def __init__(self, id_product: int ):
        self.stock = 100
        self.product_id = id_product
    

        
