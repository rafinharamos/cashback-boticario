import json
import responses
import requests

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from cashback import settings
from salesman.models import Salesman
from sales.models import Sales


class SalesTestCase(APITestCase):
    def setUp(self):
        self.salesman = Salesman.objects.create_user(
            first_name="test1",
            cpf="55165632083",
            email="teste1@test.com",
            password="teste",
        )
        self.sale = Sales.objects.create(
            code="51081789", date="2020-12-14", salesman_id=1, value=8900.0
        )
        self.data = {"cpf": self.salesman.cpf, "password": "teste"}
        response = self.client.post("/api/token/", self.data, format="json")
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {0}".format(token))

    def test_create_valid_sale(self):
        data = {"code": "51081785", "date": "2020-12-15", "value": 8900.0}
        response = self.client.post("/sales/create-sale", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content),
            {"code": "51081785", "date": "2020-12-15", "value": 8900.0},
        )

    def test_create_sale_with_value_0(self):
        data = {"code": "51081790", "date": "2020-12-14", "value": 0}
        response = self.client.post("/sales/create-sale", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content), {"value": ["Value must be bigger than 0"]}
        )

    def test_create_sale_duplicated_code(self):
        data = {"code": "51081789", "date": "2020-12-14", "value": 200}
        response = self.client.post("/sales/create-sale", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content),
            {"code": ["Sale with this code already exists"]},
        )

    def test_create_sale_invalid_code(self):
        data = {"code": "510817", "date": "2020-12-14", "value": 200}
        response = self.client.post("/sales/create-sale", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content), {"code": ["Code must contain 8 digits"]}
        )

    def test_list_sales(self):
        response = self.client.get("/sales/list-sales")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            [
                {
                    "code": "51081789",
                    "value": 8900.0,
                    "date": "2020-12-15",
                    "cashback_percent": 20,
                    "cashback_value": 445.0,
                    "status": "V",
                }
            ],
        )


class AccumulatedChargeback(TestCase):
    def setUp(self):
        self.cpf = "96789226060"
        self.url = settings.API_TOTAL_CASHBACK

    @responses.activate
    def test_valid_chargeback_accumulated_link(self):
        responses.add(
            responses.GET,
            self.url + self.cpf,
            json={"statusCode": 200, "body": {"credit": 1015}},
        )
        resp = requests.get(self.url + self.cpf)
        self.assertEqual(resp.json(), {"statusCode": 200, "body": {"credit": 1015}})
        self.assertEqual(len(responses.calls), 1)

    @responses.activate
    def test_invalid_chargeback_accumulated_link(self):
        responses.add(
            responses.GET, self.url + self.cpf, json={"statusCode": 401, "body": {}}
        )
        resp = requests.get(self.url + self.cpf)
        self.assertEqual(resp.json(), {"statusCode": 401, "body": {}})
        self.assertEqual(len(responses.calls), 1)
