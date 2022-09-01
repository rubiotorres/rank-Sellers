from src.utils.utils import Utils


class MenuScreen:
    @staticmethod
    def print_menu_screen():
        Utils.print_log("1. Register Product\n2. Show Products\n3. Register sales\n4. Show sales\n5. Update sale\n6. "
                        "Remove sale\n7. Show sellers rank\n7. logout")
