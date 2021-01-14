from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    dj_text = request.GET.get('text', 'default')
    temp = request.GET.get('removepun', 'off')
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if temp == 'on':
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "remove punctuations", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")