from django.db import models

from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    turma = models.CharField(max_length=20)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
