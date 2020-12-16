import responses
import requests
from django.test import TestCase


class AccumulatedChargeback(TestCase):
    def setUp(self):
        self.cpf = "96789226060"

    @responses.activate
    def test_valid_chargeback_accumulated_link(self):
        responses.add(
            responses.GET,
            "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf="
            + self.cpf,
            json={"statusCode": 200, "body": {"credit": 1015}},
        )
        resp = requests.get(
            "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf="
            + self.cpf
        )
        self.assertEqual(resp.json(), {"statusCode": 200, "body": {"credit": 1015}})
        self.assertEqual(len(responses.calls), 1)

    @responses.activate
    def test_invalid_chargeback_accumulated_link(self):
        responses.add(
            responses.GET,
            "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf="
            + self.cpf,
            json={"statusCode": 401, "body": {}},
        )
        resp = requests.get(
            "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf="
            + self.cpf
        )
        self.assertEqual(resp.json(), {"statusCode": 401, "body": {}})
        self.assertEqual(len(responses.calls), 1)
