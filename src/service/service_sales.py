from src.factory.mysql_conn import MysqlConn
from src.factory.mysql_db_config import MysqlDbConfig
from src.model.sales import Sales

item_db_stock = MysqlConn()
item_db_stock.connect(MysqlDbConfig())


class ServiceSales:
    def __init__(self, service_seller):
        item_db_stock.create_table(Sales.__table__)
        self.cache_sales = {}
        self.service_seller = service_seller

    def register_sales(self, sales_info_dict):
        """
        Request items persist
        """
        new_sale = Sales(sales_info_dict)
        item_db_stock.add_element(new_sale)

    def get_sales(self):
        """
        returns all sales in database
        """
        sales_dict = {}
        sellers = self.service_seller.get_sellers()
        for seller in sellers:
            sales_dict[seller.id] = []
        returned_sales = item_db_stock.find_all(Sales)
        for sale in returned_sales:
            sales_dict[sale.seller_id].append(sale)
        self.cache_sales = returned_sales
        return sales_dict

    @staticmethod
    def delete_sale(sale_id):
        return item_db_stock.delete_row(Sales, 'id', sale_id)

    def get_sale_by_id(self, id_sale):
        return item_db_stock.find_filter(Sales, 'id', id_sale)
