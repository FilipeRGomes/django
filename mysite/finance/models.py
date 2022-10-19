from random import choices
from django.db import models
from django.urls import reverse

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    account_description = models.CharField(max_length = 250)
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    #icon = models.ImageField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('finance:detail', kwargs={'pk': self.pk})


    def register_incame(self, value):
        if value > 0:
            self.balance += value
            return f"New Balance: {self.balance}" # wil return True in future
        else:
            return f'ERRO'


    def register_expanse(self, value):
        if value > 0 and value < self.balance:
            self.balance -= value
            return f"New Balance: {self.balance}" # wil return True in future
        elif value > self.balance:
            return f"Insufficient funds"
        else:
            return f'ERRO'


class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_STATUS = (
        ('P', 'Paid'),
        ('U', 'Unpaid'),
    )
    TRANSACTION_TYPE = (
        ('E', 'Expense'),
        ('I', 'Incame'),
        ('T', 'Transfer'),
    )
    data = models.DateField('transaction date')
    transaction_description = models.CharField(max_length= 250)
    value = models.DecimalField(max_digits=20, decimal_places=2) #Ver parametros (moneyField)
    status = models.CharField(max_length=1, choices=TRANSACTION_STATUS) #DEFAULT = PAID
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE) # DEFAULT = EXPANSE
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account_1 = models.ForeignKey(Account, on_delete=models.CASCADE)
    #account_2 = models.ForeignKey(Account, on_delete=models.CASCADE)


    def __str__(self):
        return self.transaction_description