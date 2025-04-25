from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required

# Create your views here.
def skyF(request):
    contexto = {
        'titulo' : 'High-Dream Games | SkyFigther e os Aerochamas'
    }
    return render(
        request,
        'skyF/index.html',
        contexto,
    )