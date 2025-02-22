from authenticate import Authenticate

class AuthAdmin(Authenticate):
    def __init__(self):
        super().__init__()
        
    def check_auth(self):
        admin = super().check_auth()
        if admin and admin["role"] == "admin":
            return admin