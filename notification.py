class Notification:
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)


class WhatsAppNotification(Notification):
    def send(self, message):
        print("WhatsApp:", message)


notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]

for notification in notifications:
    notification.send("Hello!")