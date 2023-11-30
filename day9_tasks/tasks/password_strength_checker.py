import re


class PasswordManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if not self.validate_password(password):
            raise ValueError("Password does not meet strength criteria")

        self.users[username] = password

    def validate_password(self, password):
        # Regex pattern for strong password
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

        return re.fullmatch(pattern, password) is not None

if __name__ == "__main__":
    password_manager = PasswordManager()

    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        password_manager.register_user(username, password)
        print("User registration successful")
    except ValueError as e:
        print(e)