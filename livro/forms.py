from django import forms
from .models import Livro

class CadastroLivro(forms.ModelForm):
    # Referencia informações do formulário usando campos do Livro
    class Meta:
        model = Livro
        fields = "__all__"
        #fields = ("nome","autor","co_autor","data_cadastro","emprestado","categoria","sinopse",)