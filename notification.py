class Notification:
    def __init__(self, sender):
        self.sender = sender


class EmailNotification(Notification):
    def send(self, message):
        print("Email from",self.sender, ":",message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS from",self.sender, ":",message)


class WhatsAppNotification(Notification):
    def send(self, message):
        print("WhatsApp from",self.sender, ":",message)


notifications = [
    EmailNotification("Admin"),
    SMSNotification("Admin"),
    WhatsAppNotification("Admin")
]

for notification in notifications:
    notification.send("Meeting at 10 AM")