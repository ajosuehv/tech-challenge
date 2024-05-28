from api.database import db



class BaseModel:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def commit():
        db.session.commit()
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}