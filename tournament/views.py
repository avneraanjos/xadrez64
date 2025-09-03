from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Jogador
from .serializers import JogadorSerializer

import json

@api_view(['GET'])
def get_jogadores(request):
    if request.method == 'GET':
        jogadores = Jogador.objects.all()                          # Get all objects in Jogador's database (It returns a queryset)
        serializer = JogadorSerializer(jogadores, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)
        return Response(serializer.data)                    # Return the serialized data
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_id(request, id):
    jogador = get_object_or_404(Jogador, id=id)
    serializer = JogadorSerializer(jogador)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def jogador_manager(request):
    if player_id := request.GET['id']:
        if request.method != 'POST':
            jogador = get_object_or_404(Jogador, id=player_id)

        if request.method == 'GET':
            serializer = JogadorSerializer(jogador)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = JogadorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'PUT':
            serializer = JogadorSerializer(jogador, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            jogador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:    
        return Response(status=status.HTTP_400_BAD_REQUEST)
