from django.urls import path
from restapi import views

urlpatterns = [
    path("expenses/", views.Expense_List_Create.as_view(), name="expense-list-create")
]
