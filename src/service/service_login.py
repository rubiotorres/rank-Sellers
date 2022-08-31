from src.screens.login_screen import LoginScreen


class ServiceLogin:
    def init_login(self, service_seller):
        LoginScreen.print_login_screen()
        login_response = str(input())
        if login_response == "0":
            return None
        seller_dict = self.mount_user_dict(login_response)
        is_seller_registered = service_seller.is_seller_already_registered(seller_dict)
        if not is_seller_registered:
            if service_seller.has_less_than_five_vendors():
                LoginScreen.print_login_denied()
                return None
            else:
                is_seller_registered = service_seller.register_sellers(seller_dict)
        return is_seller_registered

    @staticmethod
    def mount_user_dict(name):
        return {
            'name': name
        }
