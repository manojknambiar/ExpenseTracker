from django.shortcuts import render

# Create your views here.

def income_view(request, *args, **kwargs):
    return render(request, "base.html", {})
