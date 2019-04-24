from django.shortcuts import render
from .forms import AddIncome

# Create your views here.

def income_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AddIncome(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.save()
            form = AddIncome()
    else:
        form = AddIncome()
    return render(request, "addIncome.html", {'form':form})
