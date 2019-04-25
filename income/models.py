from django.db import models
from datetime import datetime

# Create your models here.


class Income(models.Model):

    cat = (('salary', 'Salary'),
              ('bonus', 'Bonus'),
              ('something else', 'Something else'))       
    income = models.FloatField()
    date = models.DateField(default=datetime.now)
    category = models.CharField(max_length=7, choices=cat, default='Salary')
    biweekly = models.BooleanField(default=True)
    comments = models.TextField(blank=True, null=True)
    

