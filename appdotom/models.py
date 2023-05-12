from django.db import models

class Jogadores(models.Model):
  descricao = models.CharField(max_length = 50)
  nome = models.CharField(max_length = 20)
  time = models.CharField(max_length = 20)
  #cria a classe jogadores com as epsecificações passadas pelo usuário. Nesse caso, so foi utilizada a models.charfield com um limite máximo de caracteres
class Times(models.Model):
  nome = models.CharField(max_length = 50)
  description = models.TextField()
  País = models.CharField(max_length = 50)
# cria a classe times com as pesecificações. Nesse caso foram usadas a models.charfield e a models.textfield, que da a opcao do usuario escrever um paragrafo sobre a classe
class Estadio(models.Model):
  nome = models.CharField(max_length = 50)
  local = models.TextField()
  capacidade = models.IntegerField()
  #cria a class estadio. Neste caso foi utilizado tambem o models.integerfield para o usuario selecionar um numero inteiro e dizer a capacidade do estadio
