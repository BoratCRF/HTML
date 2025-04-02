from django.shortcuts import render

# Create your views here.
def trabalheConosco(request):
    return render(
        request,
        'trabalheConosco/index.html'
    )