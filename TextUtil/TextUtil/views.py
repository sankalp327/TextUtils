from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    temp = request.GET.get('removepun', 'off')
    print(temp)
    return HttpResponse( temp)
