from twilio.rest import Client


class twilio_text:
    def __init__(self, account_sid, auth_token, messaging_service_sid):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.messaging_service_sid = messaging_service_sid
        self.client = None

    def reconnect(self):
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, phone, message):
        message = self.client.messages.create(
            messaging_service_sid=self.messaging_service_sid,
            body=message,
            to=phone
        )
