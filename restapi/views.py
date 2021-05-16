from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView

from rest_framework.response import Response

# from django.forms.models import model_to_dict
from restapi import models, serializers


# Apiview is the simplest view

# Create your views here.


class Expense_List_Create(ListCreateAPIView):
    serializer_class = serializers.ExpenseSerializer
    queryset = models.Expense.objects.all()

    '''
    NOTE: we have commented this as we are no longer using the APIView
    def get(self, request):
        expenses = models.Expense.objects.all()
        serialized_data = serializers.ExpenseSerializer(expenses, many=True)

        """
        expenses = models.Expense.objects.all()
        all_expenses = [model_to_dict(expense) for expense in expenses]"""
        return Response(serialized_data.data, 200)

    def post(self, request):

        """
        #Since we are using serializers we do not need to store individual fields and then call objecte.create this will be handled by serializer

        amount = request.data["amount"]
        merchant = request.data["merchant"]
        description = request.data["description"]
        category = request.data["category"]
        expense = models.Expense.objects.create(
            amount=amount, merchant=merchant, description=description, category=category
        )"""

        serialized_data = serializers.ExpenseSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data, 201)"""'''


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    """
    this fuuction will take care of retriveal and deleteion of a resouurce
    Note: 'serializer_class' and 'queryset'  variable names should not be changed otherwise we d=wold run into error
    #though we are calling all(), but the view itself will retrive the data based on pk passed.

    """

    serializer_class = serializers.ExpenseSerializer
    queryset = models.Expense.objects.all()
