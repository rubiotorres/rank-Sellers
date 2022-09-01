from src.utils.utils import Utils


class ProductUtils:
    @staticmethod
    def get_product_info():
        product_name = str(input("Enter product name: "))
        product_price = str(input("Enter product price: "))
        if not product_price or not product_name:
            return None
        return {
            "name": product_name,
            "price": product_price
        }

    @staticmethod
    def call_register_product(service_product):
        product_info = ProductUtils.get_product_info()
        if product_info:
            service_product.register_product(product_info)
        else:
            Utils.print_log("Please enter correct information.")

    @staticmethod
    def call_show_products(service_product):
        str_product = ""
        for product in service_product.get_product():
            str_product += f"{str(product)}\n"
        Utils.print_log(str_product)

    @staticmethod
    def get_id_product():
        return int(input("Enter product sale id: "))
