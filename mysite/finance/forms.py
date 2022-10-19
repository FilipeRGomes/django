from django import forms
from . import models


class AccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = [
            "name",
            "account_description",
            "balance",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
        ]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = [
            "data",
            "transaction_description",
            "value",
        ]
