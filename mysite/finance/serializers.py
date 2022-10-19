from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = [
            "name",
            "account_description",
            "balance",
        ]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "name",
        ]

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = [
            "data",
            "transaction_description",
            "value",
        ]
