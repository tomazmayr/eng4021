from django.contrib import admin
from .models import Jogadores
from .models import Times
from .models import Estadio
#importa os modelos do models.py

admin.site.register(Jogadores)
admin.site.register(Times)
admin.site.register(Estadio)
#registra os modelos criados anteriormente
