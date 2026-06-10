class JobApplication:

    def __init__(self, applicant_name, experience):
        self.applicant_name = applicant_name
        self.experience = experience

    def __gt__(self, other):
        return self.experience > other.experience