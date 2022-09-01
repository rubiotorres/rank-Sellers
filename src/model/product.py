from sqlalchemy import Column, Integer, TEXT

from src.factory.base import Base


class Product(Base):
    __tablename__ = 'Product'
    id = Column("Id", Integer, primary_key=True, nullable=False)
    name = Column("Name", TEXT, nullable=False)
    price = Column("price", TEXT, nullable=False)

    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

    def get_dict_model(self):
        """
        Retorna representação da classe no formato __dict__
        """
        return self.__dict__

    def __str__(self):
        return f"Id: {self.id} | Name: {self.name} | Price: {self.price}"
