from ast import If
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Categoria, Emprestimo, Livro
from usuarios.models import Usuario
from .forms import CadastroLivro,CadastroCategoria
# Create your views here.

def inicio(request):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        # Retorna o objeto com o id enviado para a página
        livros = Livro.objects.filter(usuario = usuario)
        # Formulário do livro
        formulario = CadastroLivro()
        # Define valor inicial do campo
        formulario.fields['usuario'].initial = request.session.get('usuario')
        # Retorna as categorias do usuario no formulário
        formulario.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

        # Formulário da categoria
        fc = CadastroCategoria()
        status_categoria = request.GET.get('cadastro_categoria')

        # Para os emprestimos
        e_usuarios = Usuario.objects.all()
        # Vai usar o livros = Livro.objects.filter(usuario = usuario)

        # Livro disponíveis para emprestar
        e_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = False)

        return render(request,'paginainicial.html',{'livros':livros, 'usuario_logado':request.session.get('usuario'),'formulario':formulario,'form_categoria':fc,'status_categoria':status_categoria,'e_usuarios':e_usuarios,'e_livros':e_livros})
    else:
        return redirect('/login/?status=2')

def ver_livro(request, id):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livro = Livro.objects.get(id=id)
        # Verifica se livro é do usuário logado
        if request.session.get('usuario') == livro.usuario.id:   
            emprestimos = Emprestimo.objects.filter(livro = livro) 
            formulario = CadastroLivro()
            # Define valor inicial do campo
            formulario.fields['usuario'].initial = request.session.get('usuario')
            # Retorna as categorias do usuario no formulário
            formulario.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

            # Formulário da categoria
            fc = CadastroCategoria()

            # Para os emprestimos
            e_usuarios = Usuario.objects.all()
            livros = Livro.objects.filter(usuario = usuario)

            # Livro disponíveis para emprestar
            e_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = False)

            return render(request,'ver_livro.html',{'livro':livro,'emprestimos': emprestimos,'usuario_logado':request.session.get('usuario'),'formulario':formulario,'form_categoria':fc,'e_usuarios':e_usuarios,'livros':livros,'e_livros':e_livros})
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')

def editar_livro(request, id):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livro = Livro.objects.get(id=id)
        # Verifica se livro é do usuário logado
        if request.session.get('usuario') == livro.usuario.id:
            formulario = CadastroLivro()
            # Verifica se categoria é do usuário logado   
            categorias = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            # Pro botão cadastrar Livros
            # Define valor inicial do campo
            formulario.fields['usuario'].initial = request.session.get('usuario')
            # Retorna as categorias do usuario no formulário
            formulario.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            #
            # Formulário da categoria
            fc = CadastroCategoria()

            # Para os emprestimos
            e_usuarios = Usuario.objects.all()
            livros = Livro.objects.filter(usuario = usuario)

            # Livro disponíveis para emprestar
            e_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = False)

            return render(request,'editar_livro.html',{'livro':livro, 'categorias':categorias,'usuario_logado':request.session.get('usuario'),'formulario':formulario,'form_categoria':fc,'e_usuarios':e_usuarios,'livros':livros,'e_livros':e_livros})
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
            return redirect('/livro/inicio')
        else:
            return HttpResponse('Dados Invalidos')

def excluir_livro(request, id):
    livro = Livro.objects.get(id=id).delete()
    return redirect('/livro/inicio')

def cadastrar_categoria(request):
    form = CadastroCategoria(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    usuario = request.POST.get('usuario')

    # Salvar no banco de dados
    # Esses int servem para garantir que dados sejam do mesmo tipo
    if int(usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id = usuario)
        categoria = Categoria(nome = nome,descricao = descricao,usuario = user)
        categoria.save()
        return redirect('/livro/inicio?cadastro_categoria=1')
    else:
        return HttpResponse('Erro ao salvar categoria no bd')

def cadastrar_emprestimo(request):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
        livro_emprestado = request.POST.get('livro_emprestimo')
        # Hora irá ser defina quando for enviado ao banco de dados

        if nome_emprestado_anonimo:
            emprestimo = Emprestimo(
                nome_emprestado_anonimo = nome_emprestado_anonimo,
                livro_id = livro_emprestado
            )
        else:
            emprestimo = Emprestimo(
                nome_emprestado_id = nome_emprestado,
                livro_id = livro_emprestado
            )

    try:
        emprestimo.save()

        # Marca livro como emprestado no banco de dados
        livro = Livro.objects.get(id=livro_emprestado)
        livro.emprestado = True
        livro.save()


        return HttpResponse('Emprestimo realizado com sucesso')
    except:
        return HttpResponse('Erro no cadastrar_emprestimo')
    