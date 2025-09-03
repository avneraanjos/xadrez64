from django.urls import path

from . import views

app_name = "tournament"
urlpatterns = [
    path("", views.get_jogadores, name="get_jogadores"),
    path("<int:id>/", views.get_by_id),
    path("manager/", views.jogador_manager, name="jogador_manager"),
]