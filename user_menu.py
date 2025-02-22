from user_actions import User_actions

def user_menu(user):
    action = User_actions()
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
            action.view_services()
        elif choice == "2":
            action.filter_and_sort_services()
        elif choice == "3":
            action.add_to_cart(user)
        elif choice == "4":
            action.view_cart(user)
        elif choice == "5":
            action.view_history(user)
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")


            