from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import Income
from django.contrib.admin.widgets import AdminDateWidget


class AddIncome(ModelForm):
    class Meta:
        model = Income
        fields = ['income', 'date', 'category', 'biweekly', 'comments'] 
        widgets = {
            'date': SelectDateWidget(),}
