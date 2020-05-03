from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import (AllowAny)
from allauth.account.models import EmailAddress
from django.utils.translation import ugettext_lazy as _

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")

class ResendEmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
class ResendEmailVerification(GenericAPIView):
    serializer_class = ResendEmailVerificationSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']

        try:
            email_address = EmailAddress.objects.get(email__exact=email, verified=False)
            email_address.send_confirmation(self.request, True)
        except EmailAddress.DoesNotExist:
            return Response({'detail': _('Failed! May be already verified.')}, status=208)

        return Response({'detail': _('Verification e-mail sent.')})