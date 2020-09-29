from rest_framework import serializers
from account.models import Account
from rest_framework.exceptions import ValidationError
from django.contrib.auth import password_validation


class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, read_only=True)
    hiddenButton = serializers.CharField(style={'input_type': 'text'}, read_only=True)

    class Meta:
        model = Account
        fields = ['fname', 'lname', 'mobile', 'telephone', 'password', 'email', 'country', 'address', 'address1',
                  'city',
                  'postalZip', 'state', 'company', 'password2', 'confirm_email', 'hiddenButton']

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")

        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")

        return data

    def create(self, validated_data):
        user = super(RegistrationSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
