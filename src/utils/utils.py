import os


class Utils:
    @staticmethod
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    @staticmethod
    def print_log(msg):
        Utils.clearConsole()
        print(msg)
