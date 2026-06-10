from models.job_seeker import JobSeeker
from models.recruiter import Recruiter
from utils.exceptions import JobPortalException


class UserFactory:

    @staticmethod
    def create_user(user_type, *args):

        if user_type.lower() == "jobseeker":
            return JobSeeker(*args)

        elif user_type.lower() == "recruiter":
            return Recruiter(*args)

        raise JobPortalException("Invalid User Type")