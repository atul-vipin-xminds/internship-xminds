class Notification:

    def send(self):
        pass


class EmailNotification(Notification):

    def send(self):
        print("Email notification sent")


class SMSNotification(Notification):

    def send(self):
        print("SMS notification sent")


class WhatsAppNotification(Notification):

    def send(self):
        print("WhatsApp notification sent")