from pyzdsms import get_request, ENDPOINTS, InfoMe
from pyzdsms.types import InfoSendSMS, InfoAllSMS, InfoSMS, InfoCampaign
import json

class pyzdsms():
    def __init__(self, token_persistent):
        self.headers = {
            'Authorization': f"Bearer {token_persistent}",
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_me(self) -> InfoMe:
        """
        :return: Retorna la información de la cuenta del usuario
        """
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
        """
        :param recipient: Número de teléfono a quien se quiere enviar el SMS
        :param text: Texto del SMS
        :return: Retorna información del envio del sms
        """
        response = get_request(
            ENDPOINTS['sendsms'],
            self.headers,
            json.dumps({
                "recipient": recipient,
                "mstext": text
            }),
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

    def details_sms(self, id) -> InfoSMS:
        response = get_request(
            ENDPOINTS['detailsms'].replace("ID", id),
            self.headers
        )
        if response.status_code == 200:
            return InfoSMS(response.json())
        else:
            try:
                message = response.json()['message']
            except:
                message = "An unknown error has occurred"
            raise Exception(message)

    def get_all_sms(self, page=None) -> InfoAllSMS:
        response = get_request(
            ENDPOINTS['getallsms'] if page == None else ENDPOINTS['getallsms_paginate'].replace("PAGE", f"{page}"),
            self.headers
        )
        if response.status_code == 200:
            all_sms = InfoAllSMS(response.json())
            if page != None:
                return all_sms.getAllSMS(paginated=page!=None), all_sms.countItems(), all_sms.countPaginated()
            return all_sms.getAllSMS(paginated=page != None)
        else:
            try:
                message = response.json()['message']
            except:
                message = "An unknown error has occurred"
            raise Exception(message)

    def create_campaign(self):
        return zdcampaign(self)

class zdcampaign():

    def __init__(self, self_pyzdsms):
        self.campaign_name = ""
        self.recipients = []
        self.text_sms = ""
        self.self_pyzdsms = self_pyzdsms

    def addName(self, campaign_name):
        self.campaign_name = campaign_name
        return self

    def addRecipients(self, phone):
        self.recipients.append(phone)
        return self

    def setText(self, text_sms):
        self.text_sms = text_sms
        return self

    def send(self):
        if self.campaign_name == "":
            raise Exception("You must add a name to the campaign")
        elif self.text_sms == "":
            raise Exception("You must add the text to send by sms.")
        elif len(self.recipients) == 0:
            raise Exception("You must add at least one sms receiver")

        response = get_request(
            ENDPOINTS['sendcampaign'],
            headers=self.self_pyzdsms.headers,
            payload=json.dumps({
                "name": self.campaign_name,
                "mstext": self.text_sms,
                "recipients": self.recipients
            }),
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

    def getAll(self):
        response = get_request(
            ENDPOINTS['allcampaign'],
            headers=self.self_pyzdsms.headers,
        )
        if response.status_code == 200:
            campaigns = response.json()
            response_campaigns = []
            for c in campaigns:
                response_campaigns.append(InfoCampaign(c))
            return response_campaigns
        else:
            try:
                message = response.json()['message']
            except:
                message = "An unknown error has occurred"
            raise Exception(message)
