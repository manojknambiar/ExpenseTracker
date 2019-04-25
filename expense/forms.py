from django.forms import ModelForm
from .models import ExpenseCategory

class AddCategory(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name', 'monthlyLimit'] 
