from src.factory.mysql_conn import MysqlConn
from src.factory.mysql_db_config import MysqlDbConfig
from src.model.product import Product

item_db_stock = MysqlConn()
item_db_stock.connect(MysqlDbConfig())


class ServiceProduct:
    def __init__(self):
        item_db_stock.create_table(Product.__table__)
        self.cache_products = {}

    @staticmethod
    def is_seller_already_registered(product_info_dict):
        return item_db_stock.find_filter(Product, 'name', product_info_dict['name'])

    def register_product(self, product_info_dict):
        """
        Sellers data persist
        """
        check_registered = self.is_seller_already_registered(product_info_dict)
        if not check_registered:
            new_product = Product(product_info_dict)
            item_db_stock.add_element(new_product)
            self.cache_products[new_product.id] = new_product
            return new_product
        else:
            return None or check_registered

    def get_product(self):
        """
        returns all product in database
        """
        returned_product = item_db_stock.find_all(Product)
        self.cache_products = returned_product
        return returned_product

    @staticmethod
    def get_product_by_id(product_id):
        return item_db_stock.find_filter(Product, 'id', product_id)
