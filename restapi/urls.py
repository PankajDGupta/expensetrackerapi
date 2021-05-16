from django.urls import path
from restapi import views

urlpatterns = [
    path("expenses/", views.Expense_List_Create.as_view(), name="expense-list-create"),
    path(
        "expenses/<pk>",
        views.ExpenseRetrieveDelete.as_view(),
        name="expense-retrieve-delete",
    ),
]
