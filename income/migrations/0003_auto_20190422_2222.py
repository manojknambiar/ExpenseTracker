# Generated by Django 2.1.7 on 2019-04-22 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_income_incomedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='incomeDate',
            new_name='date',
        ),
    ]