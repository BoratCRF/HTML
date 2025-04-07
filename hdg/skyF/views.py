from django.shortcuts import render

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