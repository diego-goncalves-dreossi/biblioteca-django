from django.urls import path
from . import views


app_name = 'livro'
urlpatterns = [
    path('inicio/',views.inicio, name="inicio"),
    path('livro_info/<int:id>',views.ver_livro,name="ver_livro")
]


