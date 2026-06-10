class ResumeManager:

    def upload_resume(self):
        print("Resume uploaded successfully")


class PremiumFeatures:

    def premium_support(self):
        print("Premium support is available")


class PremiumMember(ResumeManager, PremiumFeatures):
    pass