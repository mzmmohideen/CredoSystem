from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('yes')
    return render(request, 'index.html')
    # HttpResponse()
