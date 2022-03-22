from datetime import datetime
from django import template
# Criação de filtros, métodos que modificam como algo vai ser exibido.

register = template.Library()

@register.filter()
def mostra_duracao(valor1,valor2):
    # Verifica se variaveis é de um certo tipo
    if all((isinstance(valor1,datetime) , isinstance(valor2,datetime))):
        dias = (valor1 - valor2).days
        texto = 'dias'
        if dias == 1:
            texto = 'dias'
        return f"{dias} {texto}"
        
    else:
        return "Ainda não foi devolvido"
