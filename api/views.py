# Models
from api.models import Player, Game
from django.contrib.auth.models import User
# Serializers
from api.serializers import PlayerSerializer, UserSerializer, GameSerializer
# Permissions
# from api.permissions import
# Rest Framework
from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Player.objects.annotate_fields()


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('player__player_name',)

    def get_queryset(self):
        queryset = Game.objects.all()
        return queryset


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
