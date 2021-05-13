from django.test import TestCase
from restapi import models


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
