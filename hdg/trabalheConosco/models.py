from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    telefone = models.TextField(max_length=14)
    email = models.EmailField(max_length=255)
    curriculo = models.FileField(upload_to='')
    mensagem = models.TextField(max_length=2048)