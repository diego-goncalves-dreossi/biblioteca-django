from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Categoria, Emprestimo, Livro
from usuarios.models import Usuario
from .forms import CadastroLivro,CadastroCategoria
from django.db.models import Q
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

        # Livros já emprestados
        d_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = True)
      
        

        total_livros = livros.count()

        return render(request,'paginainicial.html',
        {
            'livros':livros,
            'usuario_logado':request.session.get('usuario'),'formulario':formulario,
            'form_categoria':fc,
            'status_categoria':status_categoria,
            'e_usuarios':e_usuarios,
            'e_livros':e_livros,
            'total_livros':total_livros,
            'livros_emprestados':d_livros
        })
    else:
        return redirect('/login/?status=2')

def ver_livro(request, id):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        # Pega a instancia usuário que esta logada do banco de dados
        usuario = Usuario.objects.get(id=request.session['usuario'])
        # Pega a instancia livro do banco de dados
        livro = Livro.objects.get(id=id)
        # Verifica se livro é do usuário logado
        if request.session.get('usuario') == livro.usuario.id: 
            # Pega instancias do emprestimo do banco de dados   
            emprestimos = Emprestimo.objects.filter(livro = livro) 
            # Cria o formulário
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

            # Livros já emprestados
            d_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = True)
        
            

            total_livros = livros.count()

            return render(request,'ver_livro.html',
            {
                'livro':livro,
                'emprestimos': emprestimos,
                'usuario_logado':request.session.get('usuario'),'formulario':formulario,
                'form_categoria':fc,
                'e_usuarios':e_usuarios,
                'livros':livros,
                'e_livros':e_livros,
                'total_livros':total_livros,
                'livros_emprestados':d_livros
            })
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')

def editar_livro(request, id):
    # Verifica se usuário está logado
    if request.session.get('usuario'):
        # Pega a instancia usuário que esta logada do banco de dados
        usuario = Usuario.objects.get(id=request.session['usuario'])
        # Pega a instancia livro do banco de dados
        livro = Livro.objects.get(id=id)
        # Verifica se livro é do usuário logado
        if request.session.get('usuario') == livro.usuario.id:
            # Cria formulário
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

            # Livros já emprestados
            d_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = True)
        
            

            total_livros = livros.count()

            return render(request,'editar_livro.html',
            {
                'livro':livro, 
                'categorias':categorias,
                'usuario_logado':request.session.get('usuario'),'formulario':formulario,
                'form_categoria':fc,
                'e_usuarios':e_usuarios,
                'livros':livros,
                'e_livros':e_livros,
                'total_livros':total_livros,
                'livros_emprestados':d_livros
            })
        else:
            return HttpResponse('Este livro não é seu')
    else:
        return redirect('/login/?status=2')

def cadastrar_livro(request):
    # Evita que a url seja acessada manualmente
    if request.method == 'POST':
        # Cria formulário
        formulario = CadastroLivro(request.POST)

        # Cadastra o livro no banco de dados
        if formulario.is_valid:
            formulario.save()
            return redirect('/livro/inicio')
        else:
            return HttpResponse('Dados Invalidos')

def excluir_livro(request, id):
    # Exclui do banco de dados
    livro = Livro.objects.get(id=id).delete()
    return redirect('/livro/inicio')

def cadastrar_categoria(request):
    # Captura informações da requisição e torna em váriaveis
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
        # Captura informações da requisição e torna em váriaveis
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

        return redirect('/livro/inicio')
        #return HttpResponse('Emprestimo realizado com sucesso')
    except:
        return HttpResponse('Erro no cadastrar_emprestimo')

def devolver_livro(request):
    # Atualizar livro
    id = request.POST.get('id_livro_devolver') # do livro
    livro_devolver = Livro.objects.get(id=id)
    livro_devolver.emprestado = False
    livro_devolver.save()

    # Atualizar empréstimo
    # Q é consultas no banco de dados
    emprestimo_devolver = Emprestimo.objects.get(Q(livro = livro_devolver) & Q(data_devolucao = None) )
    emprestimo_devolver.data_devolucao = datetime.now() 
    emprestimo_devolver.save()

    return redirect('/livro/inicio')

def alterar_livro(request):
    # Captura informações da requisição e torna em váriaveis
    livro_id = request.POST.get('livro_id')
    nome_livro =request.POST.get('nome_livro')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    sinopse = request.POST.get('sinopse')
    categoria_id = request.POST.get('categoria_id')
    categoria = Categoria.objects.get(id = categoria_id)
    livro = Livro.objects.get(id = livro_id)
    
    # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
    if livro.usuario.id == request.session['usuario']:
        livro.nome = nome_livro
        livro.autor = autor
        livro.co_autor = co_autor
        livro.sinopse = sinopse
        livro.categoria = categoria
        livro.save()
        return redirect(f'/livro/livro_info/{livro_id}')
    else:
        return redirect('/sair')

def seus_emprestimos(request):
    # Traz instancias do banco de dados
    usuario = Usuario.objects.get(id = request.session['usuario'])
    emprestimos = Emprestimo.objects.filter(nome_emprestado = usuario)
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

    # Livros já emprestados
    d_livros = Livro.objects.filter(usuario = usuario).filter(emprestado = True)
      
        

    total_livros = livros.count()
    

    return render(request,'seus_emprestimos.html', 
    {
        'usuario_logado':request.session.get('usuario'),'emprestimos':emprestimos,
        'livros':livros,
        'usuario_logado':request.session.get('usuario'),'formulario':formulario,
        'form_categoria':fc,
        'status_categoria':status_categoria,
        'e_usuarios':e_usuarios,
        'e_livros':e_livros,
        'total_livros':total_livros,
        'livros_emprestados':d_livros
    })

def processa_avaliacao(request):
    # Captura informações da requisição e torna em váriaveis
    id_emprestimo = request.POST.get('id_emprestimo')
    opcoes = request.POST.get('opcoes')
    id_livro = request.POST.get('id_livro')
   
    

    emprestimo = Emprestimo.objects.get(id = id_emprestimo)
    # Impede que possamos avaliar um empréstimo que não seja nosso
    if emprestimo.livro.usuario.id == request.session['usuario']:
        emprestimo.avaliacao = opcoes
        emprestimo.save()
    
        return redirect(f'/livro/livro_info/{id_livro}')
    else:
        return HttpResponse('Esse empréstimo não é seu')