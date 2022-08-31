class LoginScreen:
    @staticmethod
    def print_login_screen():
        print("Welcome to the system")
        print("Please enter the name of the current seller or 0 to exit:")

    @staticmethod
    def print_login_denied():
        print("Your user is not allowed access, check the registered users below:")

    @staticmethod
    def print_login_accepted(name):
        print(f"Welcome{name}!!!")
