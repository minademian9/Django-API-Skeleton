from rest_framework.response import Response
from rest_framework.decorators import api_view

from character.models import Character
from .serializers import characterSerializer

# @api_view(['GET'])
# def getData(request):
#     person = {'name': 'test', 'age': '30'}
#     return Response(person)


@api_view(['GET'])
def getData(request):
    all_characters = Character.objects.all()
    serializer = characterSerializer(all_characters, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = characterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data)