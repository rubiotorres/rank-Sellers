from src.factory.mysql_conn import MysqlConn
from src.factory.mysql_db_config import MysqlDbConfig
from src.model.sales import Sales

item_db_stock = MysqlConn()
item_db_stock.connect(MysqlDbConfig())


class ServiceSales:
    def __init__(self):
        item_db_stock.create_table(Sales.__table__)
        self.cache_sales = {}

    def register_sales(self, sales_info_dict):
        """
        Request items persist
        """
        new_sale = Sales(sales_info_dict)
        item_db_stock.add_element(new_sale)
        self.cache_sales[new_sale.id] = new_sale

    def get_sales(self):
        """
        returns all sales in database
        """
        returned_sales = item_db_stock.find_all(Sales)
        self.cache_sales = returned_sales
        return returned_sales
