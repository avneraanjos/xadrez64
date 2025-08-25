from django.urls import path
from . import views

urlpatterns = [
    path("rodada/<int:rodada_numero>/gerar/", views.gerar_pareamento, name="gerar_pareamento"),
]
