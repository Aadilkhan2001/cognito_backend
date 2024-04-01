from rest_framework import views, status
from rest_framework.response import Response 

from services import aws_cognito_service
from auth_cognito.serializers import (RegisterSerializer,
                                      LoginSerializer,
                                      VerificationCodeRequestSerializer,
                                      ResendCodeRequestSerializer,)

class RegisterApiView(views.APIView):
    def post(self, request):
        request_data = RegisterSerializer(data=request.data)
        if request_data.is_valid():
            try:
                response = aws_cognito_service.register(request=request_data.data)
                return Response(data=response, status=status.HTTP_200_OK)
            except aws_cognito_service.client.exceptions.UsernameExistsException:
                return Response(data={"error": "A user with this email already exists. Please use a different email address."}, status=status.HTTP_400_BAD_REQUEST)
            except aws_cognito_service.client.exceptions.InvalidPasswordException:
                return Response(data={"error": "Invalid password. Password must be at least 8 characters long and include a combination of letters, numbers, and special characters."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception:
                return Response(data={"error": "Unable to register user due to a technical issue. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=request_data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(views.APIView):
    def post(self, request):
        request_data = LoginSerializer(data=request.data)
        if request_data.is_valid():
            try:
                response = aws_cognito_service.obtain_token(request=request_data.data)
                return Response(data=response, status=status.HTTP_200_OK)
            except aws_cognito_service.client.exceptions.NotAuthorizedException:
                return Response(data={"error": "Invalid email or password. Please check your credentials and try again."}, status=status.HTTP_404_NOT_FOUND)
            except aws_cognito_service.client.exceptions.UserNotConfirmedException:
                return Response(data={"error": "User account is not yet verified. Please check your email for verification instructions."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response(data={"error": "Unable to login due to a technical issue. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=request_data.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeApiView(views.APIView):
    def post(self, request):
        request_data = VerificationCodeRequestSerializer(data=request.data)
        if request_data.is_valid():
            try:
                response = aws_cognito_service.verify_code(request=request_data.data)
                return Response(data=response, status=status.HTTP_200_OK)
            except aws_cognito_service.client.exceptions.ExpiredCodeException:
                return Response(data={"error": "Verification code has expired. Please request a new verification code."}, status=status.HTTP_400_BAD_REQUEST)
            except aws_cognito_service.client.exceptions.UserNotFoundException:
                return Response(data={"error": "Invalid email address. Please provide a valid email address."}, status=status.HTTP_404_NOT_FOUND)
            except aws_cognito_service.client.exceptions.CodeMismatchException:
                return Response(data={"error": "Invalid code. Please provide a valid code."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print("e", e)
                return Response(data={"error": "Unable to verify the code due to a technical issue. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=request_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ResendCodeApiView(views.APIView):
    def post(self, request):
        request_data = ResendCodeRequestSerializer(data=request.data)
        if request_data.is_valid():
            try:
                response = aws_cognito_service.resend_code(request=request_data.data)
                return Response(data=response, status=status.HTTP_200_OK)
            except aws_cognito_service.client.exceptions.UserNotFoundException:
                return Response(data={"error": "Invalid email address. Please provide a valid email address."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response(data={"error": "Unable to send verification code due to a technical issue. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=request_data.errors, status=status.HTTP_400_BAD_REQUEST)