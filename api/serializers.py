from rest_framework import serializers

from api.models import *


class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'transactions')


class ProductSerializer(serializers.ModelSerializer):
    sales_person = serializers.ReadOnlyField(source='sales_person.username')

    class Meta:
        model = Product
        fields = ('prod_id', 'display_name', 'cost', 'brand', 'sales_person')


class AddressSerializer(serializers.ModelSerializer):
    sales_person = serializers.ReadOnlyField(source='sales_person.username')

    class Meta:
        model = Address
        fields = ('add_id', 'house_no', 'street_name', 'locality', 'landmark', 'city', 'state_or_province', 'pincode',
                  'sales_person')


class CustomerSerializer(serializers.ModelSerializer):
    sales_person = serializers.ReadOnlyField(source='sales_person.username')

    class Meta:
        model = Customer
        fields = ('cust_id', 'cust_name', 'email', 'contact', 'add', 'sales_person')


class TransactionSerializer(serializers.ModelSerializer):
    sales_person = serializers.ReadOnlyField(source='sales_person.username')

    class Meta:
        model = Transaction
        fields = ('trans_id', 'customer', 'product', 'sales_person', 'cost', 'timestamp')
