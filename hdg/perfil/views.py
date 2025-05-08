from django.shortcuts import render

# Create your views here.
def perfil(request):
    contexto = {
        'titulo' : 'High-Dream Games | Perfil'
    }
    
    return render(
        request,
        'perfil/index.html',
        contexto
    )