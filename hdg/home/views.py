from django.shortcuts import render

from home.models import Inscritos

# Create your views here.
def home(request):
    contexto = {
        'titulo' : 'High-Dream Games | Home',
        'inscritos': Inscritos.objects.all(),
    }
    return render(
        request,
        'home/index.html',
        contexto,
    )

def gravarsub(request):
    novo_inscrito = Inscritos()
    novo_inscrito.emailsub = request.POST.get("emailsub")
    novo_inscrito.save()

    return home(request)