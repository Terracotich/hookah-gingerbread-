import json

cart = []

SERVICES_FILE = 'services.json'
HISTORY = 'history.json'
USERS = 'users.json'

class Config():
    def __init__(self):
        self.history = self.load_history()
        self.services = self.load_services()
        self.users = self.load_users()

     
    def load_services(self):
        try:
            with open(SERVICES_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
            
    def save_services(self):
            with open(SERVICES_FILE, 'w', encoding='utf-8') as file:
                json.dump(self.services,file, indent=4)

    def load_history(self):
            try:
                with open(HISTORY, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (FileNotFoundError):
                return []
    
    def save_history(self):
        with open(HISTORY, 'w', encoding='utf-8') as file:
            json.dump(self.history, file, indent=4)

    def load_users(self):
        try:
            with open (USERS, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []