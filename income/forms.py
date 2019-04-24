from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, Textarea
from .models import Income



class AddIncome(ModelForm):
    class Meta:
        model = Income
        fields = ['income', 'date', 'category', 'biweekly', 'comments'] 
        widgets = {
            'date': SelectDateWidget(),
            'comments':Textarea(attrs={'rows':3, 'cols':30}),
            }
