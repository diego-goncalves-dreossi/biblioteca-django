from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuarios.models import Usuario
# Create your views here.

def inicio(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario']).nome
        # Retorna o objeto com o id enviado para a página
        return HttpResponse(f'Olá {usuario}')
    else:
        return redirect('/login/?status=2')
