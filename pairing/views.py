from django.shortcuts import render, redirect
from .models import Jogador, Rodada, Partida
from swissdutch.dutch import DutchPairingEngine
from swissdutch.player import Player
from swissdutch.constants import FloatStatus

def gerar_pareamento(request, rodada_numero):
    jogadores_db = Jogador.objects.all()
    jogadores = []

    for j in jogadores_db:
        jogadores.append(
            Player(name=j.nome,
                   rating=j.rating,
                   title=None,
                   pairing_no=j.id,
                   score=j.pontuacao,
                   float_status=FloatStatus.none,
                   opponents=(),
                   colour_hist=())
        )

    engine = DutchPairingEngine()
    result = engine.pair_round(rodada_numero, jogadores)

    rodada = Rodada.objects.create(numero=rodada_numero)

    for p in result:
        if p.opponents:
            oponente_id = p.opponents[-1]
            try:
                oponente = Jogador.objects.get(id=oponente_id)
                # Evita criar partida duplicada
                if not Partida.objects.filter(rodada=rodada, jogador_brancas__in=[j.id, oponente_id],
                                              jogador_pretas__in=[j.id, oponente_id]).exists():
                    Partida.objects.create(
                        rodada=rodada,
                        jogador_brancas=j,
                        jogador_pretas=oponente
                    )
            except Jogador.DoesNotExist:
                pass

    return redirect("listar_partidas", rodada_numero=rodada_numero)
