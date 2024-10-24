from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "homepage/home.html", {})

def home(request):
    return render(request, "homepage/home.html", {})