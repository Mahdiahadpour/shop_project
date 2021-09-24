from rest_framework import serializers
from customers.models import Customer, Address


class UserSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = Customer
        fields = ['username', 'password', 'password_check', 'email', 'image', 'first_name', 'last_name', 'birthday',
                  'ID_card_number', 'mobile_number', 'home_number',
                  ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        new_customer = Customer(
            first_name=self._validated_data['first_name'],
            last_name=self._validated_data['last_name'],
            username=self._validated_data['username'],
            email=self._validated_data['email'],
            ID_card_number=self._validated_data['ID_card_number'],
            # date_entered=self._validated_data['date_entered'],
            mobile_number=self._validated_data['mobile_number'],
            home_number=self._validated_data['home_number'],
            birthday=self._validated_data['birthday'],
            image=self.validated_data['image']
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


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
