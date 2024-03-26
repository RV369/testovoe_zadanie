from datetime import date, timedelta

from django.shortcuts import redirect
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Achievement, Person
from .serializers import (
    AchievementSerializer,
    PersonCountSerializer,
    PersonSerializer,
)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class PersonCountViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonCountSerializer


@api_view(['GET'])
def count_person(request):
    person = Person.objects.all()
    serializer = PersonCountSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def data_list(request):
    if request.method == 'GET' and Person.objects.all().count() == 0:
        # Тестовая персона Маргарита Олеговна разговаривает по английски
        person = Person.objects.create(
            person_name='Маргарита Олеговна',
            language='en',
        )
        achievement = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=55,
            created_on=date.today() - timedelta(1),
            description='Хорошо станцевала',
            person=person,
        )
        person.achievements.add(
            achievement,
            through_defaults={'achievement': achievement},
        )
        achievement = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=45,
            created_on=date.today() - timedelta(1),
            description='Хорошо станцевала',
            person=person,
        )
        person.achievements.add(
            achievement,
            through_defaults={'achievement': achievement},
        )
        # Тестовая персона Виктория Олеговна
        person = Person.objects.create(
            person_name='Виктория Олеговна',
            language='ru',
        )
        achievement = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=22,
            created_on=date.today() - timedelta(1),
            description='Сдал отчет',
            person=person,
        )
        person.achievements.add(
            achievement,
            through_defaults={'achievement': achievement},
        )
        # Тестовая персона Анна Ивановна и её 7 достижений
        person = Person.objects.create(
            person_name='Анна Ивановна',
            language='ru',
        )
        achievement_1 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=2,
            created_on=date.today(),
            description='Хорошо станцевала',
            person=person,
        )
        achievement_2 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=20,
            created_on=date.today() - timedelta(1),
            description='Хорошо станцевала',
            person=person,
        )
        achievement_3 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=12,
            created_on=date.today() - timedelta(2),
            description='Хорошо станцевала',
            person=person,
        )
        achievement_4 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=30,
            created_on=date.today() - timedelta(3),
            description='Хорошо станцевала',
            person=person,
        )
        achievement_5 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=5,
            created_on=date.today() - timedelta(4),
            description='Хорошо станцевала',
            person=person,
        )
        achievement_6 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=15,
            created_on=date.today() - timedelta(5),
            description='Хорошо станцевала',
            person=person,
        )
        achievement_7 = Achievement.objects.create(
            name_achievements='Пустилась в пляс',
            number_of_points=26,
            created_on=date.today() - timedelta(6),
            description='Хорошо станцевала',
            person=person,
        )
        person.achievements.add(
            achievement_1,
            through_defaults={'achievement': achievement_1},
        )
        person.achievements.add(
            achievement_2,
            through_defaults={'achievement': achievement_2},
        )
        person.achievements.add(
            achievement_3,
            through_defaults={'achievement': achievement_3},
        )
        person.achievements.add(
            achievement_4,
            through_defaults={'achievement': achievement_4},
        )
        person.achievements.add(
            achievement_5,
            through_defaults={'achievement': achievement_5},
        )
        person.achievements.add(
            achievement_6,
            through_defaults={'achievement': achievement_6},
        )
        person.achievements.add(
            achievement_7,
            through_defaults={'achievement': achievement_7},
        )
        return redirect('/api/person/')
    elif request.method == 'DELETE':
        Person.objects.all().delete()
        return redirect('/api/person/')
    return redirect('/api/person/')
