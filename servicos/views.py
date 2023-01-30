from django.shortcuts import render
from django.http import HttpResponse

def servicos(request):
    return render(request, 'servicos.html')

# Create your views here.
