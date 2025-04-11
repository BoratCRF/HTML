from django.db import models

# Create your models here.

class Inscritos(models.Model):
    id_inscrito = models.AutoField(primary_key=True)
    emailsub = models.TextField(max_length=100)