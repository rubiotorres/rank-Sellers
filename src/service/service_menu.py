class ServiceMenu:
    @staticmethod
    def print_menu_screen():
        print("1. Register Product")
        print("2. Show Products")
        print("3. Register sales")
        print("4. Show sales")
        print("5. Show sellers rank")
        print("6. logout")

    @staticmethod
    def call_register_product(service_product):
        product = {
            "name": str(input("Enter product name: ")),
            "price": str(input("Enter product price: "))

        }
        product_response = service_product.register_product(product)

    @staticmethod
    def call_show_products(service_product):
        for product in service_product.get_product():
            print(product.id, product.name, product.price)

    @staticmethod
    def call_register_sales(service_sales, service_product, service_seller, seller):
        product_id = int(input("Enter product product_id: "))
        amount_product = int(input("Enter amount of product: "))
        product = service_product.get_product_by_id(product_id)
        sale = {
            "seller_name": seller.name,
            "customer_name": str(input("Enter customer name: ")),
            "product_name": product.name,
            "amount": product.price * amount_product
        }
        seller.sales = seller.sales + amount_product
        service_seller.update_sellers(seller)
        return service_sales.register_sales(sale)

    @staticmethod
    def call_show_sales(service_sales):
        for sale in service_sales.get_sales():
            print(sale.id, sale.seller_name, sale.customer_name, sale.date_sale, sale.product_name, sale.amount)

    @staticmethod
    def call_show_sellers_rank(service_sellers):
        for seller in service_sellers.get_sellers():
            print(seller.id, seller.name, seller.sales)

    def init_menu(self, service_product, service_sales, service_seller, seller):
        self.print_menu_screen()
        menu_response = int(input())
        if menu_response == 1:
            self.call_register_product(service_product)
        elif menu_response == 2:
            self.call_show_products(service_product)
        elif menu_response == 3:
            self.call_register_sales(service_sales, service_product, service_seller, seller)
        elif menu_response == 4:
            self.call_show_sales(service_sales)
        elif menu_response == 5:
            self.call_show_sellers_rank(service_seller)
        else:
            return False
        return True
