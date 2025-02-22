from config import cart
from config import Config
from datetime import datetime

class User_actions(Config):
    def __init__(self):
        super().__init__()
        self.users = []

    def format_service(self, service):
        return f"{service ['id']} - {service['name']} - {service['price']} руб., Рейтинг: {service['rating']}, Дата: {service['added_date']}"

    def view_services(self):
        if not self.services:
            print("Нет доступных услуг")
            return
        
        print("\nДоступные услуги:")
        for service in self.services:
            print(self.format_service(service))

    def filter_and_sort_services(self):
        print("\nФильтрация и сортировка услуг:")
        min_rating = float(input("Введите минимальный рейтинг для фильтрации (например, 4.0): "))
        filtered_services = [service for service in self.services if service["rating"] >= min_rating]
        sorted_services = sorted(filtered_services, key=lambda x: x["price"])
        print("\nОтфильтрованные и отсортированные услуги:")
        for service in sorted_services:
            print(self.format_service(service))

    def add_to_cart(self, user):
        try:
            self.view_services()
            choice = int(input("Введите номер услуги, которую хотите добавить в корзину: "))

            if 1 <= choice <= len(self.services):
                cart.append(self.services[choice - 1])
                print(f"{self.services[choice - 1]['name']} добавлен в корзину.")
            else:
                print("Неверный выбор!")
        except ValueError:
            print("Введите корректное число!")

    def view_cart(self, user):
        print("\nВаша корзина:")
        if not cart:
            print("Корзина пуста.")
        else:
            for idx, item in enumerate(cart, 1):
                print(f"{idx}. {item['name']} - {item['price']} руб.")
            confirm = input("Хотите оформить заказ? (да/нет): ").strip().lower()
            if confirm == "да":
                current_date = datetime.now().strftime("%Y-%m-%d")  
                
                self.history.extend([{**item, "date": current_date} for item in cart])
                self.save_history()
                cart.clear()
                print("Заказ оформлен!")
            else:
                print("Заказ не оформлен.")

    def history_service(self, service):
        return f"{service ['id']} - {service['name']} - {service['price']} руб., Рейтинг: {service['rating']}, Дата покупки: {service['date']}"

    def view_history(self, user):
        print("\nИстория покупок:")
        history = self.load_history()

        if not history:
            print("История пуста.")
            return
        
        for item in history:
            print(self.history_service(item))
