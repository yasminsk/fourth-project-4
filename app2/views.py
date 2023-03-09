from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def saniya(request):
    return HttpResponse('<marquee><h1>saniya is a beautiful girl')
