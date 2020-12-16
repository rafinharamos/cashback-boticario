from django.test import TestCase

from sales.api.v1.serializers import CreateSalesSerializer


class TestCreateSalesSerializer(TestCase):
    def test_valid_sales_serializer(self):
        data = {"code": "51081790", "date": "2020-12-22", "value": 1000.0}

        serializer = CreateSalesSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.data == data
        assert serializer.errors == {}
