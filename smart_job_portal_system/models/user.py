from utils.exceptions import JobPortalException


class User:
    total_users = 0

    def __init__(self, name, email):
        if not self.validate_email(email):
            raise JobPortalException("Invalid Email")

        self.name = name
        self.email = email

        User.total_users += 1

    def display_details(self):
        print("\nUser Details")
        print(f"Name  : {self.name}")
        print(f"Email : {self.email}")

    @staticmethod
    def validate_email(email):
        return "@" in email

    @classmethod
    def get_total_users(cls):
        return cls.total_users