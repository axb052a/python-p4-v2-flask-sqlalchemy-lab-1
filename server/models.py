from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy_serializer import SerializerMixin

# metadata = MetaData()

db = SQLAlchemy()

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = Column(Integer, primary_key=True)
    magnitude = Column(Float)
    location = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return f"<Earthquake(id={self.id}, magnitude={self.magnitude}, location='{self.location}', year={self.year})>"