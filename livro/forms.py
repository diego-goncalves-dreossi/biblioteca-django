from django import forms
from .models import Livro

class CadastroLivro(forms.ModelForm):
    # Referencia informações do formulário usando campos do Livro
    class Meta:
        model = Livro
        fields = "__all__"
        #fields = ("nome","autor","co_autor","data_cadastro","emprestado","categoria","sinopse",)


    # Construtor
    def __init__(self,*args,**kwargs):
        # Permite rodas as funcionalidades basicas de formulário que precisamos
        super().__init__(*args,**kwargs)

        # Define o componente do campo do formulário como um elemento escondido
        self.fields['usuario'].widget = forms.HiddenInput()

# O ideal seria usar o ModelForm denovo já que existe a tabela categoria
class CadastroCategoria(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=60)

    def __init__(self,*args,**kwargs):
        # Permite rodas as funcionalidades basicas de formulário que precisamos
        super().__init__(*args,**kwargs)

        # Define o componente do campo do formulário como um elemento escondido
        self.fields['descricao'].widget = forms.Textarea()
