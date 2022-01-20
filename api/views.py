from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/player-list/',
        'Detail View': '/player-detail/<str:pk>/',
        'Create': '/player-create/',
        'Update': '/player-update/<str:pk>/',
        'Delete': '/player-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def playerList(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def playerDetail(request, pk):
    try:
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(player, many=False)
        return Response(serializer.data)
    except Exception('DoesNotExist'):
        return Response('Player does not exist')

@api_view(['POST'])
def playerCreate(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def playerUpdate(request, pk):
    player = Player.objects.get(id=pk)
    serializer = PlayerSerializer(instance=player, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def playerDelete(request, pk):
    player = Player.objects.get(id=pk)
    player.delete()
    return Response('Player has been deleted.')
