from django.urls import path

from auth_cognito.api import (RegisterApiView,
                              VerifyCodeApiView,
                              LoginApiView,
                              ResendCodeApiView,)

urlpatterns = [
    path('signup/', RegisterApiView.as_view(), name='sign-up'),
    path('verify-code/', VerifyCodeApiView.as_view(), name='verify-code'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('resend-code/', ResendCodeApiView.as_view(), name='resend-code'),
]
