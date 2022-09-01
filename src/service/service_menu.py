from src.screens.menu_screen import MenuScreen
from src.utils.product_utils import ProductUtils
from src.utils.sales_utils import SalesUtils
from src.utils.seller_utils import SellerUtils


class ServiceMenu:
    def __init__(self, service_product, service_sales, service_seller, seller):
        self.service_product = service_product
        self.service_sales = service_sales
        self.service_seller = service_seller
        self.seller = seller
        self.menu_enum = {
            1: self.register_product,
            2: self.show_product,
            3: self.register_sales,
            4: self.show_sales,
            5: self.update_sales,
            6: self.remove_sale,
            7: self.show_seller
        }

    def init_menu(self):
        MenuScreen.print_menu_screen()
        menu_response = int(input())
        if menu_response in self.menu_enum.keys():
            self.menu_enum[menu_response]()
            input("Press any button to return")
            return True
        else:
            return False

    def show_product(self):
        ProductUtils.call_show_products(self.service_product)

    def register_product(self):
        ProductUtils.call_register_product(self.service_product)

    def register_sales(self):
        SalesUtils.call_register_sales(self.service_sales, self.service_product, self.service_seller,
                                              self.seller)

    def show_sales(self):
        SalesUtils.call_show_sales(self.service_sales)

    def update_sales(self):
        SalesUtils.call_update_sales(self.service_sales, self.service_product, self.service_seller)

    def remove_sale(self):
        SalesUtils.call_remove_sales(self.service_seller)

    def show_seller(self):
        SellerUtils.call_show_sellers_rank(self.service_seller)
