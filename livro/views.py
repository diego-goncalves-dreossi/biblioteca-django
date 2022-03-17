from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Livro
from usuarios.models import Usuario
# Create your views here.

def inicio(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        # Retorna o objeto com o id enviado para a página
        livros = Livro.objects.filter(usuario = usuario)
        return render(request,'paginainicial.html',{'livros':livros})
    else:
        return redirect('/login/?status=2')

def ver_livro(request, id):
    livro = Livro.objects.get(id=id)
    return render(request,'ver_livro.html',{'livro':livro})
    
