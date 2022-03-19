from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Categoria, Emprestimo, Livro
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
    if request.session.get('usuario'):
        livro = Livro.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:   
            emprestimos = Emprestimo.objects.filter(livro = livro) 
            print(emprestimos)
            return render(request,'ver_livro.html',{'livro':livro,'emprestimos': emprestimos})
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')

def editar_livro(request, id):
    if request.session.get('usuario'):
        livro = Livro.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:   
            categorias = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            return render(request,'editar_livro.html',{'livro':livro, 'categorias':categorias})
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')
