from datetime import datetime
from user_actions import User_actions
from config import Config

class Admin_actions(Config):
    def __init__(self):
        super().__init__()
        self.user_actions = User_actions()
        
    def manage_services(self):
        while True:
            print("\nУправление услугами:")
            print("1. Добавить услугу")
            print("2. Удалить услугу")
            print("3. Вернуться в главное меню")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.add_service()
            elif choice == "2":
                self.delete_service()
            elif choice == "3":
                 break
            else:
                 print("Неверный выбор")
            
    def add_service(self):
        try:
            id = int(input("Введите уникальный ID услуги: ").strip())
            if any(service['id'] == id for service in self.services):
                print(f"Ошибка: товар с ID {id} уже существует")
                return

            name = input("Введите название услуги: ").strip()
            price = int(input("Введите цену: ").strip())
            rating = float(input("Введите рейтинг: ").strip())
            added_date = datetime.now().strftime("%Y-%m-%d")
            self.services.append({"id": id, "name": name, "price": price, "rating": rating, "added_date": added_date})
            self.save_services()
            print("Услуга добавлена.")
        except ValueError:
             print("Введите корректные данные")

    def delete_service(self):
        self.user_actions.view_services()
        answer = input("Вы точно хотите что-то удалить?\n" 
                       "Это действие нельзя отменить.\n " 
                       "Если вы хотите продолжить, то напишите что-угодно, если хотите вернуться, то напишите 'нет': ").strip().lower()
        if answer == 'нет':
             return

        try:
            idx = int(input("Введите номер услуги для удаления: ")) - 1
            if 0 <= idx < len(self.services):
                removed_service = self.services.pop(idx)
                self.save_services()
                print(f"Услуга '{removed_service['name']}' удалена.")
            else:
                print("Неверный номер!")
        except ValueError:
                    print("Введите корректное число!")

    def view_statistics(self):
        buy_history = self.load_history()
        total_price = sum(item['price'] for item in buy_history)
        return total_price
    