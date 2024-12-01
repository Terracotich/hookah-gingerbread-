from functools import reduce
from datetime import datetime

users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user", "password": "user123", "role": "user", "history": []}
]

services = [
    {"name": "Bounty", "price": 1550, "rating": 4.6, "added_date": "2022-11-20"},
    {"name": "Malibu", "price": 1320, "rating": 4.5, "added_date": "2023-10-15"},
    {"name": "Passion mango", "price": 1400, "rating": 4.6, "added_date": "2022-10-15"},
    {"name": "Green mix", "price": 1660, "rating": 4.8, "added_date": "2023-12-02"},
    {"name": "Berry juice", "price": 1520, "rating": 4.5, "added_date": "2023-11-17"},
    {"name": "Sakura", "price": 1790, "rating": 4.9, "added_date": "2023-02-16"},
    {"name": "Mojito Mood", "price": 1470, "rating": 4.6, "added_date": "2023-06-20"},
]

cart = []

def authenticate():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ") 
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    print("Неверное имя пользователя или пароль.")
    return None

def view_services():
    print("\nДоступные услуги:")
    formatted_services = map(
        lambda s: f"{s['name']} - {s['price']} руб., Рейтинг: {s['rating']}, Дата: {s['added_date']}",
        services
    )
    print("\n".join(formatted_services))

def filter_and_sort_services():
    print("\nФильтрация и сортировка услуг:")
    min_rating = float(input("Введите минимальный рейтинг для фильтрации (например, 4.0): "))
    filtered_services = filter(lambda s: s["rating"] >= min_rating, services)
    sorted_services = sorted(filtered_services, key=lambda x: x["price"])
    formatted_services = map(
        lambda s: f"{s['name']} - {s['price']} руб., Рейтинг: {s['rating']}, Дата: {s['added_date']}",
        sorted_services
    )
    print("\nОтфильтрованные и отсортированные услуги:")
    print("\n".join(formatted_services))

def add_to_cart(user):
    try:
        view_services()
        choice = int(input("Введите номер услуги, которую хотите добавить в корзину: "))
        if 1 <= choice <= len(services):
            cart.append(services[choice - 1])
            print(f"{services[choice - 1]['name']} добавлен в корзину.")
        else:
            print("Неверный выбор!")
    except ValueError:
        print("Введите корректное число!")

def view_cart(user):
    print("\nВаша корзина:")
    if not cart:
        print("Корзина пуста.")
    else:
        for idx, item in enumerate(cart, 1):
            print(f"{idx}. {item['name']} - {item['price']} руб.")
        confirm = input("Хотите оформить заказ? (да/нет): ").strip().lower()
        if confirm == "да":
            user["history"].extend(cart)
            cart.clear()
            print("Заказ оформлен!")
        else:
            print("Заказ не оформлен.")

def view_history(user):
    print("\nИстория покупок:")
    if not user["history"]:
        print("История пуста.")
    else:
        formatted_history = map(
            lambda h: f"{h['name']} - {h['price']} руб., Дата покупки: {h.get('date', 'Неизвестно')}",
            user["history"]
        )
        print("\n".join(formatted_history))

def user_menu(user):
    while True:
        print("\nМеню пользователя:")
        print("1. Просмотреть услуги")
        print("2. Фильтровать и сортировать услуги")
        print("3. Добавить услугу в корзину")
        print("4. Просмотреть корзину")
        print("5. Просмотреть историю покупок")
        print("6. Выйти")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            view_services()
        elif choice == "2":
            filter_and_sort_services()
        elif choice == "3":
            add_to_cart(user)
        elif choice == "4":
            view_cart(user)
        elif choice == "5":
            view_history(user)
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")

def manage_services():
    while True:
        print("\nУправление услугами:")
        print("1. Добавить услугу")
        print("2. Удалить услугу")
        print("3. Вернуться в главное меню")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            name = input("Введите название услуги: ").strip()
            price = float(input("Введите цену: ").strip())
            rating = float(input("Введите рейтинг: ").strip())
            added_date = datetime.now().strftime("%Y-%m-%d")
            services.append({"name": name, "price": price, "rating": rating, "added_date": added_date})
            print("Услуга добавлена.")
        elif choice == "2":
            view_services()
            try:
                idx = int(input("Введите номер услуги для удаления: ")) - 1
                if 0 <= idx < len(services):
                    removed_service = services.pop(idx)
                    print(f"Услуга '{removed_service['name']}' удалена.")
                else:
                    print("Неверный номер!")
            except ValueError:
                print("Введите корректное число!")
        elif choice == "3":
            break
        else:
            print("Неверный выбор!")

def view_statistics():
    print("\nСтатистика:")
    total_revenue = reduce(
        lambda acc, user: acc + sum(item["price"] for item in user.get("history", [])), users, 0
    )
    print(f"Общая выручка: {total_revenue} руб.")
    print(f"Количество услуг: {len(services)}")

def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Управлять услугами")
        print("2. Просмотреть статистику")
        print("3. Выйти")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            manage_services()
        elif choice == "2":
            view_statistics()
        elif choice == "3":
            break
        else:
            print("Неверный выбор!")

def main():
    print("Добро пожаловать в систему управления кальянной!")
    user = authenticate()
    if user:
        if user["role"] == "user":
            user_menu(user)
        elif user["role"] == "admin":
            admin_menu()

if __name__ == "__main__":
    main()
