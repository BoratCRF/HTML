from django.shortcuts import render

# Create your views here.
def toTheHel(request):
    return render(
        request,
        'toTheHel/index.html'
    )