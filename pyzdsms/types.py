# Tipado de los datos JSON que son respondidos por el endpoint

import json

class InfoMe:
    def __init__(self, response):
        self.json = response
        id, name, email, email_verified_at, phone, phone_verified_at, credit, credit_expire, payment_data = response.values()
        self.id = id
        self.name = name
        self.email = email
        self.email_verified_at = email_verified_at
        self.phone = phone
        self.phone_verified_at = phone_verified_at
        self.credit = credit
        self.credit_expire = credit_expire
        self.payment_data = payment_data

    def getId(self):
        return self.name

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getEmailVerifiedAt(self):
        return self.email_verified_at

    def getPhone(self):
        return self.phone

    def getPhoneVerifiedAt(self):
        return self.phone_verified_at

    def getCredit(self):
        return self.credit

    def getCreditExpire(self):
        return self.credit_expire

    def getPaymentData(self):
        return self.payment_data

    def getJson(self):
        return self.json

class InfoSendSMS:
    def __init__(self, response):
        self.json = response
        message, id  = response.values()
        self.message = message
        self.id = id

    def getMessage(self):
        return self.message

    def getId(self):
        return self.id

class InfoAllSMS:
    def __init__(self, response):
        self.json = response
        self.sms = response
        self.count_paginated = 0
        self.count_items = 0

    def getAllSMS(self, paginated=False):
        """
        :param paginated: (No obligatorio) Indica si quiere obtenerse la informacion paginada
        :return: Devuelve los items de la pagina que se pide
        """
        response = []
        if not paginated:
            for r in self.sms:
                response.append(InfoSMS(r))
        else:
            data = self.sms['data']
            for r in data:
                response.append(InfoSMS(r))
            self.count_paginated = self.sms['last_page']
            self.count_items = self.sms['per_page']
        return response

    def countPaginated(self):
        """
        :return: Devuelve la cantidad de paginas
        """
        return self.count_paginated

    def countItems(self):
        """
        :return: Devuelve la cantidad de items en la pagincacion si se usa
        """
        return self.count_items

class InfoSMS:
    def __init__(self, response):
        self.json = response
        id, recipient, mstext, sms_count, via, status, created_at = response.values()
        self.id = id
        self.recipient = recipient
        self.mstext = mstext
        self.sms_count = sms_count
        self.via = via
        self.status = status
        self.created_at = created_at

    def getId(self):
        return self.id

    def getRecipient(self):
        return self.recipient

    def getText(self):
        return self.mstext

    def getSmsCount(self):
        return self.sms_count

    def getVia(self):
        return self.via

    def getStatus(self):
        return self.status

    def getCreatedAt(self):
        return self.created_at

class InfoCampaign:
    def __init__(self, response):
        self.json = response
        id, name, recipients, mstext, sms_count, via, status, user_id, created_at, delivered = response.values()
        self.id = id
        self.name = name
        self.recipients = recipients
        self.mstext = mstext
        self.sms_count = sms_count
        self.via = via
        self.status = status
        self.user_id = user_id
        self.created_at = created_at
        self.delivered = delivered

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getRecipients(self):
        return json.loads(self.recipients)

    def getText(self):
        return self.mstext

    def getSmsCount(self):
        return self.sms_count

    def getVia(self):
        return self.via

    def getStatus(self):
        return self.status

    def getUserId(self):
        return self.user_id

    def getCreatedAt(self):
        return self.created_at

    def getDelivered(self):
        return self.delivered
