from config import Config

class Authenticate(Config):
    def __init__(self):
        super().__init__

    def authenticate(self):
        self.username = input("Введите логин: ")
        self.password = input("Введите пароль: ")
        return self.check_auth()

    def check_auth(self):
        for user in self.load_users():
            if user["username"] == self.username and user["password"] == self.password:
                return user
        print("Неверное имя пользователя или пароль")
        return None
        
        