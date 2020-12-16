import json

from rest_framework import status
from rest_framework.test import APITestCase

from salesman.models import Salesman


class SalesmanTestCase(APITestCase):
    def setUp(self):
        Salesman.objects.create_user(
            first_name="test1",
            cpf="55165632083",
            email="teste1@test.com",
            password="teste",
        )
        Salesman.objects.create_user(
            first_name="test2",
            cpf="18389059010",
            email="teste2@test.com",
            password="teste",
        )
        Salesman.objects.create_user(
            first_name="test3",
            cpf="58905959032",
            email="teste3@test.com",
            password="teste",
        )
        Salesman.objects.create_user(
            first_name="test4",
            cpf="46263810068",
            email="teste4@test.com",
            password="teste",
        )

    def test_registration_salesman(self):
        data = {
            "name": "test5",
            "cpf": "20801176026",
            "email": "teste5@test.com",
            "password": "teste",
        }
        response = self.client.post("/salesman/create-salesman/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_duplicated_cpf(self):
        data = {
            "name": "test6",
            "cpf": "18389059010",
            "email": "teste6@test.com",
            "password": "teste",
        }
        response = self.client.post("/salesman/create-salesman/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content),
            {"cpf": ["This cpf is already registered"]},
        )

    def test_registration_duplicated_email(self):
        data = {
            "name": "test7",
            "cpf": "34914918005",
            "email": "teste1@test.com",
            "password": "teste",
        }
        response = self.client.post("/salesman/create-salesman/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content),
            {"email": ["salesman with this email address already exists."]},
        )

    def test_registration_validated_cpf_only_numbers(self):
        data = {
            "name": "test8",
            "cpf": "551.656.320-83",
            "email": "teste8@test.com",
            "password": "teste",
        }
        response = self.client.post("/salesman/create-salesman/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content),
            {"cpf": ["Only numbers of cpf is allowed"]},
        )

    def test_registration_cpf_is_not_valid(self):
        data = {
            "name": "test8",
            "cpf": "55165632099",
            "email": "teste8@test.com",
            "password": "teste",
        }
        response = self.client.post("/salesman/create-salesman/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content),
            {"cpf": ["This cpf is invalid"]},
        )

    def test_salesman_login(self):
        data = {"cpf": "55165632083", "password": "teste"}
        response = self.client.post("/api/token/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
