from django.shortcuts import render

# Create your views here.
def toTheHel(request):
    contexto = {
        'titulo' : 'High-Dream Games | To The Hel'
    }
    return render(
        request,
        'toTheHel/index.html',
        contexto,
    )