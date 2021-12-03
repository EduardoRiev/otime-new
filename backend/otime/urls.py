from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from card.api.viewsets import cardViewSet
from turma.api.viewsets import TurmaViewSet
from professor.api.viewsets import professorViewSet
from disciplina.api.viewsets import disciplinaViewSet
from sala.api.viewsets import salaViewSet, tipoViewSet, ferramentaViewSet
from escola.api.viewsets import escolaViewSet

rotas = routers.DefaultRouter()
rotas.register(r'cards', cardViewSet)
rotas.register(r'turmas', TurmaViewSet)
rotas.register(r'professores', professorViewSet)
rotas.register(r'disciplinas', disciplinaViewSet)
rotas.register(r'salas', salaViewSet)
rotas.register(r'tiposDeSala', tipoViewSet)
rotas.register(r'ferramentasDeSala', ferramentaViewSet)
rotas.register(r'escolas', escolaViewSet)

urlpatterns = [
    path('', include(rotas.urls)),
    path('admin/', admin.site.urls),
]
