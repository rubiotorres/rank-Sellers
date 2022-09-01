from src.utils.product_utils import ProductUtils
from src.utils.seller_utils import SellerUtils
from src.utils.utils import Utils


class SalesUtils:
    @staticmethod
    def call_register_sales(service_sales, service_product, service_seller, seller):
        product_id = int(input("Enter product product_id: ") or 0)
        amount_product = int(input("Enter amount of product: ") or 0)
        if not product_id or not amount_product:
            Utils.print_log("Please enter correct information.")
            return False
        product = service_product.get_product_by_id(product_id)

        SellerUtils.update_seller_info(service_seller, seller, amount_product)

        sale = {
            "seller_id": seller.id,
            "customer_name": str(input("Enter customer name: ")),
            "product_id": product.id,
            "amount": int(amount_product) * int(product.price)
        }
        return service_sales.register_sales(sale)

    @staticmethod
    def call_show_sales(service_sales):
        str_sales = ""
        for _, list_sales in service_sales.get_sales().items():
            for sale in list_sales:
                str_sales+=f"{str(sale)}\n"
        Utils.print_log(str_sales)

    @staticmethod
    def call_remove_sales(service_sales):
        id_sale = ProductUtils.get_id_product()
        if not id_sale:
            return False

        service_sales.delete_sale(id_sale)
        return service_sales.register_sales(id_sale)

    @staticmethod
    def call_update_sales(service_sales, service_product, service_seller):
        id_sale = ProductUtils.get_id_product()
        if not id_sale:
            return False

        old_sale = service_sales.get_sale_by_id(id_sale)
        Utils.print_log(old_sale)

        product_id = input("Enter product product_id (blank to the same): ")
        amount_product = input("Enter amount of product (0 to the same): ")
        seller_name = str(input("Enter seller name (0 to the same): ") or old_sale.seller_name)
        customer_name = str(input("Enter customer name (0 to the same): ") or old_sale.customer_name)

        old_seller = service_seller.get_seller_by_id(old_sale.seller_id)
        old_product = service_product.get_product_by_id(old_sale.product_id)

        if seller_name:
            seller = service_seller.is_seller_already_registered({'name': seller_name})
            if not seller:
                return None
        else:
            seller = old_seller

        if product_id:
            product = service_product.get_product_by_id(int(product_id))
            if not product:
                return False
        else:
            product = old_product

        if amount_product:
            amount = int(amount_product) * int(product.price)
        else:
            amount = old_sale.amount
        service_sales.delete_sale(id_sale)

        sale = {
            "id": old_sale.id,
            "seller_id": seller.id,
            "customer_name": customer_name,
            "date_sale": old_sale.date_sale,
            "product_id": product.id,
            "amount": amount
        }
        SellerUtils.update_seller_info(service_seller, old_seller, - int(old_sale.amount) / int(old_product.price))
        SellerUtils.update_seller_info(service_seller, seller, amount_product)
        return service_sales.register_sales(sale)
