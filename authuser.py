from authenticate import Authenticate

class AuthUser(Authenticate):
    def __init__(self):
        super().__init__()
        
    def check_auth(self):
        user = super().check_auth()
        if user and user["role"] == "user":
            return user