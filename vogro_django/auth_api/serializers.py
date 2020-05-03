from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
 
UserModel = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'is_volunteer')
        read_only_fields = ('email', )

class TokenSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    # Serializer for Token model.
    class Meta:
        model = Token
        fields = ('key', 'user')

class CustomRegisterSerializer(RegisterSerializer):
    is_volunteer = serializers.IntegerField(
        required=False,
        default=-1,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['is_volunteer'] = self.validated_data.get('is_volunteer', '')
        return data_dict