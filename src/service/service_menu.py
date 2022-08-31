class ServiceMenu:
    @staticmethod
    def print_menu_screen():
        print("1. Register Product")
        print("2. Show Products")
        print("3. Register sales")
        print("4. Show sales")
        print("5. Update sale")
        print("5. Remove sale")
        print("6. Show sellers rank")
        print("7. logout")

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
            "seller_id": seller.id,
            "customer_name": str(input("Enter customer name: ")),
            "product_id": product.id,
            "amount": int(amount_product) * int(product.price)
        }
        sales = seller.sales + amount_product
        service_seller.update_sellers(seller, sales)
        return service_sales.register_sales(sale)

    @staticmethod
    def call_show_sales(service_sales):
        for _, list_sales in service_sales.get_sales().items():
            for sale in list_sales:
                print(sale)

    @staticmethod
    def call_show_sellers_rank(service_sellers):
        for seller in service_sellers.get_sellers():
            print(seller)

    @staticmethod
    def call_remove_sales(service_sales):
        id_sale = int(input("Enter product sale id: "))
        if not id_sale:
            return False
        service_sales.delete_sale(id_sale)
        return service_sales.register_sales(id_sale)

    @staticmethod
    def call_update_sales(service_sales, service_product, service_seller):
        id_sale = int(input("Enter product sale id: "))
        if not id_sale:
            return False
        old_sale = service_sales.get_sale_by_id(id_sale)
        print(old_sale)

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
        old_sale_amount = old_seller.sales - int(old_sale.amount) / int(old_product.price)
        service_seller.update_sellers(old_seller, old_sale_amount)

        sales = seller.sales + int(amount) / int(product.price)
        service_seller.update_sellers(seller, sales)

        return service_sales.register_sales(sale)

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
            self.call_update_sales(service_sales, service_product, service_seller)
        elif menu_response == 6:
            self.call_remove_sales(service_seller)
        elif menu_response == 7:
            self.call_show_sellers_rank(service_seller)
        else:
            return False
        return True
