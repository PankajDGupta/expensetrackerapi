from django.test import TestCase
from restapi import models
from django.urls import reverse  # we are using this to track back the urls in restapi


class TestModels(TestCase):
    # please not ethe test methods should always start withh "test_"
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=200, merchant="amazon", description="amc hadphone", category="music"
        )
        inserted_exp = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(200, inserted_exp.amount)
        self.assertEqual("amazon", inserted_exp.merchant)
        self.assertEqual("amc hadphone", inserted_exp.description)
        self.assertEqual("music", inserted_exp.category)


class TestViews(TestCase):
    def test_expense_create(self):
        payload = {
            "amount": 50,
            "merchant": "ATnT",
            "description": "Cell phone desc",
            "category": "utilities",
        }

        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )
        self.assertEqual(
            201, res.status_code
        )  # for creation we get 201 as the status code
        json_response = res.json()
        self.assertEqual(payload["amount"], json_response["amount"])
        self.assertEqual(str(payload["merchant"]), json_response["merchant"])
        self.assertEqual(str(payload["description"]), json_response["description"])
        self.assertEqual(str(payload["category"]), json_response["category"])
        self.assertIsInstance(json_response["id"], int)

    def test_expense_list(self):
        res = self.client.get(reverse("restapi:expense-list-create"), format="json")
        self.assertEqual(200, res.status_code)
        json_res = res.json()
        self.assertIsInstance(json_res, list)
        expenses = models.Expense.objects.all()
        self.assertEqual(len(expenses), len(json_res))

    def test_expense_create_required_fields_missing(self):
        # this is a negative test where we are testing that if a required field is not sent then  the app should return 400 response

        payload = {
            "merchant": "ATnT",
            "description": "Cell phone desc",
            "category": "utilities",
        }
        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )

        # print("test_expense_create_required_fields_missing :" + str(res.status_code))
        self.assertEqual(400, res.status_code)
