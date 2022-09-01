from src.envs.environment_variable import IS_TEST
from src.factory.mysql_conn import MysqlConn
from src.factory.mysql_db_config import MysqlDbConfig
from src.model.seller import Seller

item_db_stock = MysqlConn()
if not IS_TEST:
    item_db_stock.connect(MysqlDbConfig())
    item_db_stock.create_table(Seller.__table__)


class ServiceSellers:
    def __init__(self):
        self.cache_sellers = {}

    @staticmethod
    def is_seller_already_registered(sellers_info_dict):
        return item_db_stock.find_filter(Seller, 'name', sellers_info_dict['name'])

    @staticmethod
    def has_less_than_five_vendors():
        return item_db_stock.count_rows(Seller) >= 5

    def register_sellers(self, sellers_info_dict):
        """
        Sellers data persist
        """
        new_sellers = Seller(sellers_info_dict)
        item_db_stock.add_element(new_sellers)
        self.cache_sellers[new_sellers.id] = new_sellers
        return new_sellers

    def get_sellers(self):
        """
        returns all sellers in database
        """
        returned_seller = item_db_stock.find_all_desc(Seller, Seller.sales)
        self.cache_sellers = returned_seller
        return returned_seller

    @staticmethod
    def update_sellers(seller, sales):
        """
        update sellers in database
        """
        returned_seller = item_db_stock.update_element_seller(seller, sales)
        return returned_seller

    def get_seller_by_id(self, id_seller):
        return item_db_stock.find_filter(Seller, 'id', id_seller)
