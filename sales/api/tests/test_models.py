import datetime

from django.test import TestCase
from sales.models import Sales
from salesman.models import Salesman


class SalesModelTest(TestCase):
    def setUp(self):
        Salesman.objects.create_user(
            first_name="test1",
            cpf="55165632083",
            email="teste1@test.com",
            password="teste",
        )

    def test_sales_model(self):
        sales = Sales(code="51081789", date="2020-12-15", salesman_id=1, value=8900.0)
        sales.save()
        self.assertEqual(sales.code, "51081789")
        self.assertEqual(sales.date, datetime.date(2020, 12, 15))
        self.assertEqual(sales.salesman.id, 1)
        self.assertEqual(sales.value, 8900.0)
