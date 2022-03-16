from django.urls import path
from . import views


app_name = 'livro'
urlpatterns = [
    path('cadastrar/',views.cadastrar),
]


