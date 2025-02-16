from django.shortcuts import render
# Create your views here.


#HTTP request
def home(request):
    #return HTTP response
    return render(request, 'recipes/pages/home.html', context={ 'name': 'Luan',})

