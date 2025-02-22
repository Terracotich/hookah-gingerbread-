from authenticate import Authenticate
from user_menu import user_menu
from admin_menu import Admin_menu


def main():
    authenticate = Authenticate()
    print("Добро пожаловать в систему управления кальянной!")
    user = authenticate.authenticate()
    if user:
        if user["role"] == "user":
            user_menu(user)
        elif user["role"] == "admin":
            admin_menu = Admin_menu()
            admin_menu.display_menu()

if __name__ == "__main__":
    main()

#хеширование логинов
