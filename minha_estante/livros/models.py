from django.db import models

class Livro(models.Model):
    STATUS_CHOICES = [
        ('quero_ler', 'Quero Ler'),
        ('lendo', 'Lendo'),
        ('lido', 'Lido'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='quero_ler')
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self): ## Método especial que define como o objeto (Livro) vai ser tratado.
        return self.titulo




