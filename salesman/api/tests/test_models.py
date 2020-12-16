from django.test import TestCase

from salesman.models import Salesman


class SalesmanModelTest(TestCase):
    def test_salesman_model(self):
        salesman = Salesman(
            first_name="test1",
            cpf="55165632083",
            email="teste1@test.com",
            password="teste",
        )
        salesman.save()
        self.assertEqual(salesman.first_name, "test1")
        self.assertEqual(salesman.cpf, "55165632083")
        self.assertEqual(salesman.email, "teste1@test.com")
        self.assertEqual(salesman.password, "teste")
