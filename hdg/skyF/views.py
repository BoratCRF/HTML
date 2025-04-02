from django.shortcuts import render

# Create your views here.
def skyF(request):
    return render(
        request,
        'skyF/index.html'
    )