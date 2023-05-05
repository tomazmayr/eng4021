from django.shortcuts import render

from .models import Jogadores, Estadio, Times

def home(request):
  return render(request, "home.html")

def list_futebol(request):
  jogadores = Jogadores.objects.all()
  estadio = Estadio.objects.all()
  times = Times.objects.all()
  context = { "Jogadores": jogadores, "Estadios": estadio, "Times": times }
  return render(request, "atributos.html", context=context)

