from sqlalchemy import Column, DateTime, Integer, TEXT, func

from src.factory.base import Base
from src.service.service_product import ServiceProduct
from src.service.service_sellers import ServiceSellers

service_seller = ServiceSellers()
service_product = ServiceProduct()


class Sales(Base):
    __tablename__ = 'Sales'
    id = Column("Id", Integer, primary_key=True)
    seller_id = Column("SellerId", Integer, nullable=False)
    customer_name = Column("customerName", TEXT, nullable=False)
    date_sale = Column("date_sale", DateTime, server_default=func.now())
    product_id = Column("ProductId", Integer, nullable=False)
    amount = Column("amount", Integer, nullable=False)

    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

    def get_dict_model(self):
        """
        Retorna representação da classe no formato __dict__
        """
        return self.__dict__

    def __str__(self):
        seller = service_seller.get_seller_by_id(self.seller_id)
        product = service_product.get_product_by_id(int(self.product_id))
        return f"Id: {str(self.id)} | Seller Name: {seller.name} | Customer Name: {self.customer_name} | Date: {str(self.date_sale)} | Product Name: {product.name} | Amount: {str(self.amount)}\n"
