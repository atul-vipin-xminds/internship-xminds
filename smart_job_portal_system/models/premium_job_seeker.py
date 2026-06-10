from models.job_seeker import JobSeeker


class PremiumJobSeeker(JobSeeker):

    def __init__(self, name, email, skills, membership_type):
        super().__init__(name, email, skills)
        self.membership_type = membership_type

    def priority_apply(self):
        print(
            f"{self.name} used Priority Apply ({self.membership_type} Membership)"
        )