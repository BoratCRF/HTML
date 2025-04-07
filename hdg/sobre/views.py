from django.shortcuts import render

# Create your views here.
def sobre(request):
    contexto = {
        'titulo' : 'High-Dream Games | Sobre'
    }
    return render(
        request,
        'sobre/index.html',
        contexto,
    )