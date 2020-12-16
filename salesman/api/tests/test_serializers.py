from django.test import TestCase

from salesman.api.v1.serializers import CreateSalesmanSerializer


class TestCreateSalesmanSerializer(TestCase):
    def test_valid_salesman_serializer(self):
        data = {
            "name": "test5",
            "cpf": "90714545090",
            "email": "teste6@test.com",
            "password": "teste",
        }

        serializer = CreateSalesmanSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.data == data
        assert serializer.errors == {}
