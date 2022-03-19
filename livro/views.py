from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Categoria, Emprestimo, Livro
from usuarios.models import Usuario
from .forms import CadastroLivro
# Create your views here.

def inicio(request):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        # Retorna o objeto com o id enviado para a página
        livros = Livro.objects.filter(usuario = usuario)
        formulario = CadastroLivro()
        return render(request,'paginainicial.html',{'livros':livros, 'usuario_logado':request.session.get('usuario'),'formulario':formulario})
    else:
        return redirect('/login/?status=2')

def ver_livro(request, id):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        livro = Livro.objects.get(id=id)
        # Verifica se livro é do usuário logado
        if request.session.get('usuario') == livro.usuario.id:   
            emprestimos = Emprestimo.objects.filter(livro = livro) 
            formulario = CadastroLivro()
            return render(request,'ver_livro.html',{'livro':livro,'emprestimos': emprestimos,'usuario_logado':request.session.get('usuario'),'formulario':formulario})
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')

def editar_livro(request, id):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        livro = Livro.objects.get(id=id)
        # Verifica se livro é do usuário logado
        if request.session.get('usuario') == livro.usuario.id:
            # Verifica se categoria é do usuário logado   
            categorias = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            return render(request,'editar_livro.html',{'livro':livro, 'categorias':categorias,'usuario_logado':request.session.get('usuario')})
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')


def cadastrar_livro(request):
    # Evita que a url seja acessada manualmente
    if request.method == 'POST':
        formulario = CadastroLivro(request.POST)

        if formulario.is_valid:
            formulario.save()
            return HttpResponse("Livro salvo com sucesso!")

        else:
            return HttpResponse('Dados Invalidos')
            livros = Livro.objects.filter(usuario = usuario)
            formulario = CadastroLivro()
            return render(request,'paginainicial.html',{'livros':livros, 'usuario_logado':request.session.get('usuario'),'formulario':formulario})

        return HttpResponse(formulario)
