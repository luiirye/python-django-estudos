from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista.html', {'livros': livros})
def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/detalhe.html', {'livro': livro})

def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/adicionar.html', {'form': form})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/editar.html', {'form': form})

def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'livros/deletar.html', {'livro': livro})