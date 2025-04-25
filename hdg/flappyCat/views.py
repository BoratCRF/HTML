from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required

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