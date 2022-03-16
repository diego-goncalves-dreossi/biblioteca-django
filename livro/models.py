from mailbox import NotEmptyError
from django.db import models
from datetime import date

# Create your models here.

class Livro(models.Model):
    # Colunas da tabela
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    co_autor = models.CharField(max_length=100,blank=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=100,blank=True,null=True)
    data_emprestimo = models.DateTimeField(blank=True,null=True)
    data_devolucao = models.DateTimeField(blank=True,null=True)
    tempo_duracao = models.DateField(blank=True,null=True)


    def __str__(self):
        return self.nome