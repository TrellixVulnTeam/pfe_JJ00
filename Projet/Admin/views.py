
from django.shortcuts import render
from django.db import models


# Create your views here.


def index(request):
    return render(request, "index.html")
