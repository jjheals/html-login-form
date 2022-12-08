from hashlib import sha256

class User: 

    def __init__(self, username, password):
        self.username = username
        self.password = User.encrypt(password)

    @staticmethod
    def encrypt(pw):
        return sha256(pw.encode('utf-8')).hexdigest()