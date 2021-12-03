from django.db import models
from sala.models import Sala

class Escola(models.Model):
    nome = models.CharField(max_length = 100)
    periodo_letivo = models.CharField(max_length = 100)
    aulas_por_turno = models.IntegerField()
    dia_por_semana = models.IntegerField()
    salas = models.ManyToManyField(Sala)

    def __str__(self):
        return "Escola #%d: %s" % (int(self.id), self.nome)

    class Meta:
        db_table = 'escola'
        verbose_name_plural = 'Escolas'