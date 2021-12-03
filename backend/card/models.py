from django.db import models
from disciplina.models import Disciplina
from turma.models import Turma
from sala.models import Sala

# Create your models here.
class Card(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE)
    opcoes = (
        (1, "Simples"),
        (2, "Duplo"),
        (3, "Terço"),
        (4, "Quarto"),
        (5, "Quinto"),
        (6, "Sexto"),
    )
    sequencia = models.IntegerField(choices = opcoes)
    dias = (
        (1, "Segunda-feira"),
        (2, "Terça-feira"),
        (3, "Quarta-feira"),
        (4, "Quinta-feira"),
        (5, "Sexta-feira")
    )
    dia = models.IntegerField(choices = dias)
    horarios = (
        (1, "7:00 - 7:45"),
        (2, "7:45 - 8:30"),
        (3, "8:50 - 9:35"),
        (4, "9:35 - 10-20"),
        (5, "10:30 - 11:15"),
        (6, "11:15 - 12:00"),

        (7, "13:00 - 13:45"),
        (8, "13:45 - 14:30"),
        (9, "14:50 - 15:35"),
        (10, "15:35 - 16:20"),
        (11, "16:30 - 17:15"),
        (12, "17:15 - 18:00"),
    )
    horario = models.IntegerField(choices = horarios)
    def __str__(self):
        return "Card #%d: %s" % (int(self.id), self.disciplina)

    class Meta:
        db_table = 'Card'
        verbose_name_plural = 'Cards'