from django.shortcuts import render

# Create your views here.
def flappyCat(request):
    return render(
        request,
        'flappyCat/index.html'
    )