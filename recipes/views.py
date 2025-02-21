from django.shortcuts import render
# Create your views here.


#HTTP request
def home(request):
    #return HTTP response
    return render(request, 'recipes/pages/home.html', context={ 'name': 'Luan',})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luan Avila',
    })

