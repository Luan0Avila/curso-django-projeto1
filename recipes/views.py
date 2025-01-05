from django.http import HttpResponse
from django.shortcuts import render

#HTTP request
def home(request):
    #return HTTP response
    return render(request, 'recipes/home.html',)

def sobre(request):
    #return HTTP response
    return HttpResponse('sobre')


def contato(request):
    #return HTTP response
    return render(request, 'recipes/contatos.html')