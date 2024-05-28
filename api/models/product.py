from api.database import db
from api.models.base_model import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Product(BaseModel,db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.TEXT)
    cost = db.Column(db.Float)
    price = db.Column(db.Float)
    sku = db.Column(UUID(as_uuid=True), primary_key=False, default=uuid.uuid4)


    def __init__(self, name: str, cost: float, price: float ):
        self.name = name
        self.cost = cost
        self.price = price
