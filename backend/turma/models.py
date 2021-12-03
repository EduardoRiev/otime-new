from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length = 100)
    abreviatura = models.CharField(max_length = 25, null = True, blank = True)

    def __str__(self):
        return "Turma #%d: %s" % (int(self.id), self.nome)

    class Meta:
        db_table = 'Turma'
        verbose_name_plural = 'Turmas'