from sqlalchemy import Column, Integer, String
from database import Base

class FruitDB(Base):
    __tablename__ = 'fruits_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)