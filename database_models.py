from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()
class product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    disc = Column(String)
    price = Column(Float)
    quant = Column(Integer)

    
