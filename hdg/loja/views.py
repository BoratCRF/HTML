from django.shortcuts import render

# Create your views here.
def loja(request):
    contexto = {
        'titulo' : 'High-Dream Games | Loja'
    }
    
    return render(
        request,
        'loja/index.html',
        contexto
    )