from django import forms
from .models import Livro

class CadastroLivro(forms.ModelForm):
    # Referencia informações do formulário usando campos do Livro
    class Meta:
        model = Livro
        fields = "__all__"
        #fields = ("nome","autor","co_autor","data_cadastro","emprestado","categoria","sinopse",)

    # Construtor
    def __init__(self,*args, **kwargs):
        # Permite que os métodos que precisamos de formulário ainda funcionem nessa sobrescrição (Polimorfismo)
        super().__init__()
        # Define o componente do campo do formulário como um elemento escondido
        self.fields['usuario'].widget = forms.HiddenInput()