from models.user import User
from models.job_seeker import JobSeeker
from models.recruiter import Recruiter
from models.premium_job_seeker import PremiumJobSeeker
from models.premium_member import PremiumMember
from models.notifications import (
    EmailNotification,
    SMSNotification,
    WhatsAppNotification
)
from models.job_application import JobApplication
from models.database import Database
from models.factory import UserFactory
from models.strategy import (
    JobSearch,
    SkillSearch,
    LocationSearch,
    SalarySearch
)
from utils.exceptions import JobPortalException


try:

    print("\n--- Factory Pattern ---")

    job_seeker = UserFactory.create_user(
        "jobseeker",
        "Neha",
        "neha@gmail.com",
        ["Python", "SQL"]
    )

    recruiter = UserFactory.create_user(
        "recruiter",
        "Kiran",
        "kiran@gmail.com",
        "Innovate Solutions"
    )

    print("\n--- Job Seeker Details ---")
    job_seeker.display_details()
    job_seeker.apply_job("Python Developer")

    print("\n--- Recruiter Details ---")
    recruiter.display_details()
    recruiter.post_job("Backend Developer")

    print("\n--- Premium Job Seeker ---")

    premium_user = PremiumJobSeeker(
        "Arjun",
        "arjun@gmail.com",
        ["Python", "Django"],
        "Gold"
    )

    premium_user.priority_apply()

    print("\n--- Multiple Inheritance ---")

    member = PremiumMember()
    member.upload_resume()
    member.premium_support()

    print("\n--- Notification System ---")

    notifications = [
        EmailNotification(),
        SMSNotification(),
        WhatsAppNotification()
    ]

    for notification in notifications:
        notification.send()

    print("\n--- Operator Overloading ---")

    applicant1 = JobApplication("Rahul", 5)
    applicant2 = JobApplication("Anjali", 3)

    if applicant1 > applicant2:
        print(f"{applicant1.applicant_name} has more experience")
    else:
        print(f"{applicant2.applicant_name} has more experience")

    print("\n--- Singleton Pattern ---")

    db1 = Database()
    db2 = Database()

    print("db1 == db2 :", db1 == db2)

    print("\n--- Strategy Pattern ---")

    search = JobSearch(SkillSearch())
    search.search_jobs()

    search.set_strategy(LocationSearch())
    search.search_jobs()

    search.set_strategy(SalarySearch())
    search.search_jobs()

    print("\n--- Class Method ---")
    print("Total Users :", User.get_total_users())

except JobPortalException as e:
    print("Error:", e)

finally:
    print("\nProgram Ended")