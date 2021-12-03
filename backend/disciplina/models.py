from django.db import models
from professor.models import Professor
from sala.models import Sala

# Create your models here.
class Disciplina (models.Model):
    nome = models.CharField(max_length = 100)
    abreviatura = models.CharField(max_length = 25, null = True, blank = True)
    credito = models.IntegerField(null = True)
    professores = models.ManyToManyField(Professor)
    locais = models.ManyToManyField(Sala)

    def __str__(self):
        return "Disciplina #%d: %s" % (int(self.id), self.nome)

    class Meta:
        db_table = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
