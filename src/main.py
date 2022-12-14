from src.service.service_login import ServiceLogin
from src.service.service_menu import ServiceMenu
from src.service.service_product import ServiceProduct
from src.service.service_sales import ServiceSales
from src.service.service_sellers import ServiceSellers

service_seller = ServiceSellers()
service_login = ServiceLogin()
service_product = ServiceProduct()
service_sales = ServiceSales(service_seller)


def main():
    system_login = True
    while system_login:
        system_execute = True
        is_logged = service_login.init_login(service_seller)
        if not is_logged:
            for seller in service_seller.get_sellers():
                print(seller)
            return
        else:
            while system_execute:
                system_execute = ServiceMenu(service_product, service_sales, service_seller, is_logged).init_menu()


if __name__ == '__main__':
    main()
