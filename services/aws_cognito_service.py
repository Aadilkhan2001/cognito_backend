import boto3

from django.conf import settings

class AwsCognitoService(object):
    def __init__(self) -> None:
        self.client = boto3.client('cognito-idp', settings.AWS_REGION)

    def register(self, request):
        response = self.client.sign_up(
            ClientId=settings.AWS_COGNITO_CLIENT_ID,
            Username=request['email'],
            Password=request['password'],
            UserAttributes=[
                {
                    'Name': 'name',
                    'Value': request['name'],
                }
            ]
        )
        return response
    
    def verify_code(self, request):
        response = self.client.confirm_sign_up(
            ClientId=settings.AWS_COGNITO_CLIENT_ID,
            Username=request['email'],
            ConfirmationCode=request['code']
        )
        return response

    def obtain_token(self, request):
        response = self.client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': request['email'],
                'EMAIL': request['email'],
                'PASSWORD': request['password']
            },
            ClientId=settings.AWS_COGNITO_CLIENT_ID,
        )
        return response


    def resend_code(self, request):
        response = self.client.resend_confirmation_code(
            ClientId=settings.AWS_COGNITO_CLIENT_ID,
            Username=request['email'],
        )
        return response

aws_cognito_service = AwsCognitoService()