from datetime import date

from tests import *
from tests.helpers import MyHelper
from tests import tests_helper
import unittest
import pytest
import os
from parasut.client import Client


class TestExample(unittest.TestCase):
    # def test_helper(self):
    #     self.assertEqual(MyHelper.days_ago(date.today()), 0)

    # def test_other_helper(self):
    #     assert tests_helper.list_has(3, [1, 2, 3])

    # def test_pass(self):
    #     self.assertEqual(True, True)

    # @pytest.mark.xfail
    # def test_should_fail(self):
    #     self.assertEqual(False, True)

    def testClientIdEnvVariable(self):
        try:
            CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
        except KeyError:
            CLIENT_ID = None
            self.assertIsNotNone(CLIENT_ID)

    def testClientSecretEnvVariable(self):
        try:
            CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
        except KeyError:
            CLIENT_SECRET = None
            self.assertIsNotNone(CLIENT_SECRET)

    def testUsernameEnvVariable(self):
        try:
            USERNAME = os.environ['PARASUT_USERNAME']
        except KeyError:
            USERNAME = None
            self.assertIsNotNone(USERNAME)

    def testPasswordEnvVariable(self):
        try:
            PASSWORD = os.environ['PARASUT_PASSWORD']
        except KeyError:
            PASSWORD = None
            self.assertIsNotNone(PASSWORD)

    def testClient00(self):
        with self.assertRaises(TypeError):
            Client()

    def testClient01(self):
        with self.assertRaises(TypeError):
            CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
            Client(client_id=CLIENT_ID)

    def testClient02(self):
        with self.assertRaises(TypeError):
            CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
            CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
            Client(client_id=CLIENT_ID,
                   client_secret=CLIENT_SECRET)

    def testClient03(self):
        with self.assertRaises(TypeError):
            CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
            CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
            USERNAME = os.environ['PARASUT_USERNAME']
            Client(client_id=CLIENT_ID,
                   client_secret=CLIENT_SECRET,
                   username=USERNAME)

    def testClient0(self):
        CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
        CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
        USERNAME = os.environ['PARASUT_USERNAME']
        PASSWORD = os.environ['PARASUT_PASSWORD']

        Client(client_id=CLIENT_ID,
               client_secret=CLIENT_SECRET,
               username=USERNAME,
               password=PASSWORD,
               sandbox=True)

    def testClient1(self):
        CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
        CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
        USERNAME = os.environ['PARASUT_USERNAME']
        PASSWORD = os.environ['PARASUT_PASSWORD']

        Client(client_id=CLIENT_ID,
               client_secret=CLIENT_SECRET,
               username=USERNAME,
               password=PASSWORD)

    def testClient2(self):
        CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
        CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
        USERNAME = os.environ['PARASUT_USERNAME']
        PASSWORD = os.environ['PARASUT_PASSWORD']

        Client(client_id=CLIENT_ID,
               client_secret=CLIENT_SECRET,
               username=USERNAME,
               password=PASSWORD,
               base_url='https://www.example.com',
               token_url='https://www.example.com/oauth/token')

    def testIndexInvoice(self):
        CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
        CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
        USERNAME = os.environ['PARASUT_USERNAME']
        PASSWORD = os.environ['PARASUT_PASSWORD']

        client_obj = Client(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            username=USERNAME,
                            password=PASSWORD,
                            sandbox=True)

        client_obj.initialize()
        client_obj.functions.indexInvoice()
        print(client_obj.companyId)

    def testCreateInvoice(self):
        CLIENT_ID = os.environ['PARASUT_CLIENT_ID']
        CLIENT_SECRET = os.environ['PARASUT_CLIENT_SECRET']
        USERNAME = os.environ['PARASUT_USERNAME']
        PASSWORD = os.environ['PARASUT_PASSWORD']

        client_obj = Client(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            username=USERNAME,
                            password=PASSWORD,
                            sandbox=True)

        client_obj.initialize()

        # You can get request parameters from
        # https://apidocs.parasut.com/#operation/createContact
        data = {
            "data": {
              "type": "contacts",
              "attributes": {
                "email": "user@example.com",
                "name": "string",
                "short_name": "string",
                "contact_type": "person",
                "tax_office": "string",
                "tax_number": "string",
                "district": "string",
                "city": "string",
                "address": "string",
                "phone": "string",
                "fax": "string",
                "is_abroad": True,
                "archived": True,
                "iban": "string",
                "account_type": "customer"
              },
              "relationships": {
                "category": {
                    "data": {
                        "type": "item_categories"
                    }
                },
                "contact_people": {
                  "data": [
                    {
                      "type": "contact_people",
                      "attributes": {
                        "name": "string",
                        "email": "user@example.com",
                        "phone": "string",
                        "notes": "string"
                      }
                    }
                  ]
                }
              }
            }
          }

        obj = client_obj.functions.createContact(data)
        print(obj.json())
