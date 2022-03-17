from django.urls import path
from . import views


app_name = 'livro'
urlpatterns = [
    path('inicio/',views.inicio, name="inicio"),
]


