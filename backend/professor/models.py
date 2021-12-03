from django.db import models

class Professor(models.Model):
	nome = models.CharField(max_length=100)
	abreviatura = models.CharField(max_length=25, null = True, blank = True)
	coordenador = models.BooleanField(default = False)

	def __str__(self):
		return "Professor #%d: %s" % (int(self.id), self.nome)

	class Meta:
		db_table = 'Professor'
		verbose_name_plural = 'Professores'
