from django.db import models

# Create your models here.

class Ferramenta(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return "Ferramenta #%d: %s" % (int(self.id), self.nome)

    class Meta:
        db_table = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'

class Tipo(models.Model):
    nome = models.CharField(max_length = 100)
    ferramentas = models.ManyToManyField(Ferramenta, blank = True)

    def __str__(self):
        return "Tipo #%d: %s" % (int(self.id), self.nome)

    class Meta:
        db_table = 'Tipo'
        verbose_name_plural = 'Tipos'

# Cria model sala

class Sala(models.Model):
    nome = models.CharField(max_length = 100)
    abreviatura = models.CharField(max_length = 25, null = True, blank = True)
    capacidade = models.IntegerField()
    tipos = models.ManyToManyField(Tipo, blank = True)

    def __str__(self):
        return "Sala #%d: %s" % (int(self.id), self.nome)

    class Meta:
        db_table = 'Sala'
        verbose_name_plural = 'Salas'
