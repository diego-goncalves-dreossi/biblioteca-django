from django import template
# Criação de filtros, métodos que modificam como algo vai ser exibido.

register = template.Library()

@register.filter()
def mostra_duracao(valor1,valor2):
    return (valor1 - valor2).days