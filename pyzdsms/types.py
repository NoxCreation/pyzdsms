
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
        message, = response.values()
        self.message = message

    def getMessage(self):
        return self.message

class InfoAllSMS:
    def __init__(self, response):
        self.json = response
        self.sms = response

    def getAllSMS(self):
        response = []
        for r in self.sms:
            response.append(InfoSMS(r))
        return response

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
