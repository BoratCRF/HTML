from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'titulo' : 'High-Dream Games | Home'
    }
    return render(
        request,
        'home/index.html',
        contexto,
    )