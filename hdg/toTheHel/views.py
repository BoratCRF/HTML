from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required

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