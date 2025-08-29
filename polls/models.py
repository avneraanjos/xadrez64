import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

class Jogador(models.Model):
    nome_completo = models.CharField(max_length=255)
    #id = models.CharField(max_length=100, primary_key=True)
    data_nascimento = models.DateField(blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='jogadores/fotos/', blank=True, null=True) # Requer 'Pillow' instalado
    data_cadastro = models.DateTimeField(default=timezone.now)
    rating_clube = models.IntegerField(blank=True, null=True)
    id_cbx = models.CharField(max_length=100, blank=True, null=True)
    rating_cbx = models.IntegerField(blank=True, null=True)
    id_fide = models.CharField(max_length=100, blank=True, null=True)
    rating_fide = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"

# class Clube(models.Model):
#     nome = models.CharField(max_length=100)
#     logo = models.ImageField(upload_to='clubes/logos/', blank=True, null=True) # Requer 'Pillow' instalado
#     jogadores = models.ManyToManyField(Jogador, related_name='clubes')
#     #torneios = models.ManyToManyField('Torneio', related_name='clubes')

#     def __str__(self):
#         return self.nome

# class Torneio(models.Model):
#     nome = models.CharField(max_length=100)
#     data_inicio = models.DateField()
#     data_fim = models.DateField()
#     #rodadas = 
#     def __str__(self):
#         return self.nome
