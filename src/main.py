from src.model.sales import Sales
from src.service.service_login import ServiceLogin
from src.service.service_menu import ServiceMenu
from src.service.service_product import ServiceProduct
from src.service.service_sales import ServiceSales
from src.service.service_sellers import ServiceSellers

service_seller = ServiceSellers()
service_login = ServiceLogin()
service_menu = ServiceMenu()
service_product = ServiceProduct()
service_sales = ServiceSales()


def main():
    system_login = True
    system_execute = True
    while system_login:
        system_execute = True
        is_logged = service_login.init_login(service_seller)
        if not is_logged:
            for seller in service_seller.get_sellers():
                print(seller.id, seller.name, seller.sales)
            return
        else:
            while system_execute:
                system_execute = service_menu.init_menu(service_product, service_sales, service_seller, is_logged)


if __name__ == '__main__':
    main()
