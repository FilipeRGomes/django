# Generated by Django 4.1.2 on 2022-10-12 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_account_balance_alter_transaction_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_desciption',
            new_name='account_description',
        ),
    ]
