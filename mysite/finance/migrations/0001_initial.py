# Generated by Django 4.1.2 on 2022-10-09 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_desciption', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='transaction date')),
                ('transaction_description', models.CharField(max_length=250)),
                ('value', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], max_length=1)),
                ('transaction_type', models.CharField(choices=[('E', 'Expense'), ('I', 'Incame'), ('T', 'Transfer')], max_length=1)),
                ('account_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.category')),
            ],
        ),
    ]
