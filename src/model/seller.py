from sqlalchemy import Column, Integer, TEXT

from src.factory.base import Base


class Seller(Base):
    __tablename__ = 'Seller'
    id = Column("Id", Integer, primary_key=True, nullable=False)
    name = Column("Name", TEXT, nullable=False)
    sales = Column("Sales", Integer, default=0)

    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

    def get_dict_model(self):
        """
        Retorna representação da classe no formato __dict__
        """
        return self.__dict__

    def __str__(self):
        return str(f"id: {self.id} | Name: {self.name} | Sales: {self.sales}")
