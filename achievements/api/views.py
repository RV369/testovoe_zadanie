from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Achievement, Person
from .serializers import (
    AchievementSerializer,
    PersonCountSerializer,
    PersonSerializer,
)


@api_view(['GET', 'POST'])
def achievement_list(request):
    if request.method == 'POST':
        serializer = AchievementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    achievement = Achievement.objects.all()
    serializer = AchievementSerializer(achievement, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def person(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response('index.html', status=status.HTTP_204_NO_CONTENT)
    serializer = PersonSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def count_person(request):
    person = Person.objects.all()
    serializer = PersonCountSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)
