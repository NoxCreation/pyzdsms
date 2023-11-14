from pyzdsms import get_request, ENDPOINTS, InfoMe
from pyzdsms.types import InfoSendSMS, InfoAllSMS


class pyzdsms():
    def __init__(self, token_persistent):
        self.headers = {
            'Authorization': f"Bearer {token_persistent}",
            'Accept': 'application/json'
        }

    def get_me(self) -> InfoMe:
        response = get_request(
            ENDPOINTS['me'],
            self.headers
        )
        if response.status_code == 200:
            return InfoMe(response.json())
        else:
            try:
                message = response.json()['message']
            except:
                message = "An unknown error has occurred"
            raise Exception(message)

    def send_sms(self, recipient, text) -> InfoSendSMS:
        response = get_request(
            ENDPOINTS['sendsms'],
            self.headers,
            {
                "recipient": recipient,
                "mstext": text
            },
            method="POST"
        )
        if response.status_code == 200:
            return InfoSendSMS(response.json())
        else:
            try:
                message = response.json()['message']
            except:
                message = "An unknown error has occurred"
            raise Exception(message)

    def details_sms(self):
        pass

    def get_all_sms(self) -> InfoAllSMS:
        response = get_request(
            ENDPOINTS['getallsms'],
            self.headers
        )
        if response.status_code == 200:
            return InfoAllSMS(response.json())
        else:
            try:
                message = response.json()['message']
            except:
                message = "An unknown error has occurred"
            raise Exception(message)
