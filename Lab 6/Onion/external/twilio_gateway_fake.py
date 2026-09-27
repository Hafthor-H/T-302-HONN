from core.application.gateway.i_sms_gateway import ISmsGateway

class TwilioGatewayFake(ISmsGateway):
    def send_sms(self, phone_number: str, message: str):
        print(f'Email to {phone_number} sent with message: {message}')
