from django.db import models

# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=20)
    monthlyLimit = models.FloatField()
