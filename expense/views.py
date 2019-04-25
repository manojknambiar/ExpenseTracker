from django.shortcuts import render
from .forms import AddCategory

# Create your views here.
def index_view(request, *args, **kwargs):
    
    return render(request, "index.html", {})


def category_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AddCategory(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.save()
            form = AddCategory()
    else:
        form = AddCategory()
    return render(request, "addCategory.html", {'form':form})
