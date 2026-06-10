from models.user import User
from utils.decorators import logger


class JobSeeker(User):

    def __init__(self, name, email, skills):
        super().__init__(name, email)
        self.skills = skills

    @logger
    def apply_job(self, job_title):
        print(f"{self.name} applied for {job_title}")