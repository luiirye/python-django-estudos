from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('<int:pk>/', views.detalhe_livro, name='detalhe_livro'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('<int:pk>/editar/', views.editar_livro, name='editar_livro'),
    path('<int:pk>/deletar/', views.deletar_livro, name='deletar_livro'),
]