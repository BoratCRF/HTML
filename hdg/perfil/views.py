from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponseForbidden

@login_required
def perfil(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Verificação para acesso ao Admin
    if request.GET.get('admin') == '1':
        if request.user.is_staff or request.user.is_superuser:
            return redirect('/admin/')
        else:
            return HttpResponseForbidden("Acesso negado.")

    if request.method == 'POST':
        # Atualizar dados do usuário
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.username = request.POST.get('username')
        email = request.POST.get('email')
        user.email = email if email else user.email

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
        return redirect('perfil')

    contexto = {
        'titulo': 'High-Dream Games | Perfil',
        'user': request.user,
        'user_profile': user_profile
    }

    return render(request, 'perfil/index.html', contexto)
