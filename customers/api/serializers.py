from rest_framework import serializers
from customers.models import Customer, Address


class UserSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = Customer
        fields = ['username', 'password', 'password_check', 'email', 'ID_card_number']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        new_customer = Customer(
            username=self._validated_data['username'],
            email=self._validated_data['email'],
            ID_card_number =self.validated_data['ID_card_number']
        )
        password = self.validated_data['password']
        password_check = self.validated_data['password_check']

        if password != password_check:
            raise serializers.ValidationError({
                'password': 'Passwords must match'
            })
        new_customer.set_password(password)
        new_customer.save()
        return new_customer


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birthday',
                  'ID_card_number', 'mobile_number', 'home_number',
                  ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'
    })

    new_password = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'
    })
    new_password_check = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = Customer
        fields = ['password', 'new_password', 'new_password_check', ]

        extra_kwargs = {
            'password': {'write_only': True},
            'new_password': {'write_only': True},
            'new_password_check': {'write_only': True},
        }
