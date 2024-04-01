from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class VerificationCodeRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ResendCodeRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()