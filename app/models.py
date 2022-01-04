from django.db import models

# Create your models here.
class Clientes(models.Model):
  nome = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  telefone = models.CharField(max_length=20)
  endereco = models.CharField(max_length=70)
  bairro = models.CharField(max_length=30)
  cidade = models.CharField(max_length=30)
  cep = models.IntegerField()