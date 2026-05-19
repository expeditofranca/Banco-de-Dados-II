from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    lider = models.CharField(max_length=100)

class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='atividades')