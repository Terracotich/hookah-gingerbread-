from admin_actions import Admin_actions

class Admin_menu():
    def __init__(self):
        self._admin_actions = Admin_actions()

    def _manage_services(self):
        self._admin_actions.manage_services()

    def _view_statistics(self):
        total_sum = self._admin_actions.view_statistics()
        print(f'Общая сумма покупок: {total_sum} руб.')

    def display_menu(self):
        while True:
            print("\nМеню администратора:")
            print("1. Управлять услугами")
            print("2. Просмотреть статистику")
            print("3. Выйти")
            choice = input("Выберите действие: ").strip()
            if choice == "1":
                self._manage_services()
            elif choice == "2":
                self._view_statistics()
            elif choice == "3":
                break
            else:
                print("Неверный выбор!")