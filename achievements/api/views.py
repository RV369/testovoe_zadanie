from api import serializers
from api.core_processor import create_data
from api.models import Achievement, Person
from django.shortcuts import redirect
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrive'):
            return serializers.PersonSerializer
        return serializers.PersonCreateSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = serializers.AchievementSerializer


@api_view(['GET'])
def count_person(request):
    person = Person.objects.all()
    serializer = serializers.PersonCountSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def data_list(request):
    if request.method == 'GET' and Person.objects.all().count() == 0:
        create_data()
        return redirect('/api/person/')
    elif request.method == 'DELETE':
        Person.objects.all().delete()
        return redirect('/api/person/')
    return redirect('/api/person/')
