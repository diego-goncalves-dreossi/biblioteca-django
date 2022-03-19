from django.db import models
from datetime import date
from usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

    def __str__(self):   
        return self.nome

class Livro(models.Model):
    # Colunas da tabela
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    co_autor = models.CharField(max_length=100,blank=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    sinopse = models.TextField(default='Sinopse')
    # Chave estrangeira que é uma Categoria e ao deletar objeto nada acontece
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING,default=1)



    def __str__(self): 
        return self.nome

class Emprestimo(models.Model):
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank = True, null = True)
    data_emprestimo = models.DateField(blank=True,null=True)
    data_devolucao = models.DateField(blank=True,null=True)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"