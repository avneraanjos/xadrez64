from django.db import models



class Torneio(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    jogadores = models.ManyToManyField(Jogador, related_name="torneios")

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    rating = models.IntegerField(default=1500)
    pontuacao = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nome} ({self.rating})"

class Rodada(models.Model):
    numero = models.IntegerField()
    data = models.DateField(auto_now_add=True)

class Partida(models.Model):
    rodada = models.ForeignKey(Rodada, on_delete=models.CASCADE)
    jogador_brancas = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name="partidas_brancas")
    jogador_pretas = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name="partidas_pretas")
    resultado = models.CharField(max_length=10, blank=True, null=True)  # ex: "1-0", "0-1", "½-½"
