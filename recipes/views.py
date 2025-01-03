from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#HTTP request
def home(request):
    #return HTTP response
    return HttpResponse('Home')

def sobre(request):
    #return HTTP response
    return HttpResponse('sobre')


def contato(request):
    #return HTTP response
    return HttpResponse('Contato')