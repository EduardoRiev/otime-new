from django.contrib import admin

from .models import Sala, Tipo, Ferramenta  # Coloca o model para ser registrado através da interface administrativa
# Register your models here.
admin.site.register(Sala) # Coloca o model para ser registrado através da interface administrativa
admin.site.register(Tipo)

admin.site.register(Ferramenta)