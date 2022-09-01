from src.utils.utils import Utils


class SellerUtils:
    @staticmethod
    def update_seller_info(service_seller, seller, amount_product):
        sales = seller.sales + amount_product
        service_seller.update_sellers(seller, sales)

    @staticmethod
    def call_show_sellers_rank(service_sellers):
        str_seller = ""
        for seller in service_sellers.get_sellers():
            str_seller+=f"{str(seller)}\n"
        Utils.print_log(str_seller)
