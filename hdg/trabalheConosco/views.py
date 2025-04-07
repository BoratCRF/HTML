from django.shortcuts import render

from trabalheConosco.models import Pessoa

# Create your views here.
def trabalheConosco(request):
    contexto = {
        'titulo' : 'High-Dream Games | Trabalhe Conosco',
        'pessoas': Pessoa.objects.all(),

    }
    return render(
        request,
        'trabalheConosco/index.html',
        contexto,
    )

def gravar(request):
    # salvar os dados da tela no banco de dados
    nova_pessoa = Pessoa()
    nova_pessoa.nome      = request.POST.get("nome")
    nova_pessoa.telefone  = request.POST.get("telefone")
    nova_pessoa.email     = request.POST.get("email")
    nova_pessoa.curriculo = request.POST.get("curriculo")
    nova_pessoa.mensagem = request.POST.get("mensagem")
    nova_pessoa.save()

    return trabalheConosco(request)