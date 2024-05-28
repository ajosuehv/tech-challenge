from api.database import db
from api.models.base_model import BaseModel
from sqlalchemy.dialects.postgresql import JSON,UUID
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.functions import now
import datetime
import uuid

class Order(BaseModel, db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    ticket_id = db.Column(UUID(as_uuid=True), primary_key=False, default=uuid.uuid4)

    def __init__(self):
        self.created_date = datetime.datetime.now()