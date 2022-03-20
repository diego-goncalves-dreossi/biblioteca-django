from django.urls import path
from . import views


app_name = 'livro'
urlpatterns = [
    path('inicio/',views.inicio, name="inicio"),
    path('livro_info/<int:id>',views.ver_livro,name="ver_livro"),
    path('livro_info/editar_livro/<int:id>',views.editar_livro,name="editar_livro"),
    path('cadastrar_livro',views.cadastrar_livro,name="cadastrar_livro"),
    path('excluir_livro/<int:id>',views.excluir_livro, name="excluir_livro")
]


