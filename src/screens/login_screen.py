from src.utils.utils import Utils


class LoginScreen:
    @staticmethod
    def print_login_screen():
        Utils.print_log("Welcome to the system!!!\nPlease enter the name of the current seller or blank to exit:")

    @staticmethod
    def print_login_denied():
        Utils.print_log("Your user is not allowed access, check the registered users below:")

    @staticmethod
    def print_login_accepted(name):
        Utils.print_log(f"Welcome{name}!!!")
