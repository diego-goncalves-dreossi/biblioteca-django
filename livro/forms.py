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
