from models.user import User


class Recruiter(User):

    def __init__(self, name, email, company_name):
        super().__init__(name, email)
        self.company_name = company_name

    def display_details(self):
        super().display_details()
        print(f"Company : {self.company_name}")

    def post_job(self, job_title):
        print(f"{self.company_name} posted '{job_title}'")