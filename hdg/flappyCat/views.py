from django.shortcuts import render

# Create your views here.
def flappyCat(request):
    contexto = {
        'titulo' : 'High-Dream Games | Flappy Cat'
    }
    return render(
        request,
        'flappyCat/index.html',
        contexto,
    )