from sqlalchemy import Column, DateTime, Integer, TEXT, func

from src.factory.base import Base


class Sales(Base):
    __tablename__ = 'Sales'
    id = Column("Id", Integer, primary_key=True)
    seller_name = Column("SellerName", TEXT, nullable=False)
    customer_name = Column("customerName", TEXT, nullable=False)
    date_sale = Column("date_sale", DateTime, server_default=func.now())
    product_name = Column("ProductName", TEXT, nullable=False)
    amount = Column("amount", Integer, nullable=False)

    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

    def get_dict_model(self):
        """
        Retorna representação da classe no formato __dict__
        """
        return self.__dict__
