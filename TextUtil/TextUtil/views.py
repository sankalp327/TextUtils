from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    dj_text = request.POST.get('text', 'default')
    temp = request.POST.get('removepun', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    new_line = request.POST.get('newline', 'off')
    count_char = request.POST.get('countchar', 'off')
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if temp == 'on':
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "remove punctuations", "analyzed_text": analyzed}
        dj_text = analyzed
    if full_caps == 'on':
        analyzed = ""
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': "to uppercase", "analyzed_text": analyzed}
        dj_text = analyzed
    if new_line == 'on':
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': "remove newline", "analyzed_text": analyzed}
        dj_text = analyzed
    if count_char == 'on':
        count = 0
        for char in dj_text:
            if char != " ":
                count += 1
        dj_text = "{0} {1}".format(dj_text, str(count))
        params = {'purpose': "count number of char", "analyzed_text": count}

    if count_char != 'on' and new_line != 'on' and full_caps != 'on' and temp != 'on':
        return HttpResponse("Error")
    else:
        return render(request, "analyze.html", params)
