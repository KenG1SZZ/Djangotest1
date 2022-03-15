from django.http import HttpResponse
from django.shortcuts import render
def respo (request) :
    return render(request, './index.html')

