# Generated by Django 2.1.7 on 2019-04-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0008_auto_20190422_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
