import re

from rest_framework import serializers
from validate_docbr import CPF

from salesman.models import Salesman


class CreateSalesmanSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, source="first_name")
    cpf = serializers.CharField(required=True)

    class Meta:
        model = Salesman
        fields = ("name", "cpf", "email", "password")

    def validate_cpf(self, value):
        cpf = CPF()
        if not bool(re.compile("^[ 0-9]+$").match(value)):
            raise serializers.ValidationError("Only numbers of cpf is allowed")
        if not cpf.validate(value):
            raise serializers.ValidationError("This cpf is invalid")
        if Salesman.objects.filter(cpf=value).exists():
            raise serializers.ValidationError("This cpf is already registered")
        return value

    def create(self, validated_data):
        salesman = Salesman.objects.create_user(**validated_data)
        return salesman
