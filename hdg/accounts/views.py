# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib import messages


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu nome completo',
            'class': 'form-control',
            'style': 'background-color: #222; color: #fff; border: 1px solid #444;'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu email',
            'class': 'form-control',
            'style': 'background-color: #222; color: #fff; border: 1px solid #444;'
        })
    )

    class Meta:
        model = UserCreationForm.Meta.model
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "As senhas não coincidem. Por favor, verifique.")

        return cleaned_data


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
