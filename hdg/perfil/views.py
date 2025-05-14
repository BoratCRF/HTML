from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile

# Create your views here.
@login_required

def perfil(request):
    contexto = {
        'titulo' : 'High-Dream Games | Perfil'
    }
    
    return render(
        request,
        'perfil/index.html',
        contexto
    )



@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Atualizar dados do usuário
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        
        # Atualizar senha (se fornecida)
        new_password = request.POST.get('password')
        if new_password:
            user.set_password(new_password)
        
        user.save()
        
        # Atualizar imagem de perfil
        if 'profile_image' in request.FILES:
            user_profile.profile_image = request.FILES['profile_image']
            user_profile.save()
        
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('profile')
    
    return render(request, 'perfil.html', {
        'user': request.user,
        'user_profile': user_profile
    })