from django.db import models

class Jogadores(models.Model):
  descricao = models.CharField(max_length = 50)
  nome = models.CharField(max_length = 20)
  time = models.CharField(max_length = 20)
  
class Times(models.Model):
  nome = models.CharField(max_length = 50)
  description = models.TextField()
  País = models.CharField(max_length = 50)

class Estadio(models.Model):
  nome = models.CharField(max_length = 50)
  local = models.TextField()
  capacidade = models.IntegerField()