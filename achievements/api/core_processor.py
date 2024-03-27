from datetime import date, timedelta

from api.models import Achievement, Person
from googletrans import Translator

translator = Translator()


def string_translate(string, dest):
    try:
        translation = translator.translate(string, dest)
    except AttributeError as e:
        return 'Translation failed: ' + str(e)
    return translation.text


def list_achievements(person):
    achievements = Achievement.objects.select_related().filter(
        person=person.pk,
    )
    achievement_list, sum_number_of_points = [], 0
    list_number_of_points = []
    for achievement in achievements:
        achievement_list.append(
            {
                'number_of_points': achievement.number_of_points,
                'created_on': achievement.created_on,
                'person': achievement.person,
            },
        )
        list_number_of_points.append(achievement.number_of_points)
        sum_number_of_points += achievement.number_of_points
    return achievement_list, sum_number_of_points, list_number_of_points


def list_person(validated_data):
    persons = []
    for person in validated_data:
        achievement_list = list_achievements(person)
        persons.append(
            {
                'pk': person.pk,
                'person_name': person.person_name,
                'language': person.language,
                'achievements_count': person.achievements.count(),
                'achievements': achievement_list[0],
                'sum_number_of_points': achievement_list[1],
                'list_number': achievement_list[2],
            },
        )
    return persons


def max_difference_in_achievement_points(persons):
    List_difference = []
    for person in persons:
        number = max(person['list_number']) - min(person['list_number'])
        List_difference.append(
            {
                'number': number,
                'person_name': person['person_name'],
            },
        )
    return List_difference


def achievements_for_7_consecutive_days(persons):
    for person in persons:
        key = 0
        key_data = [
            str(date.today()),
            str(date.today() - timedelta(1)),
            str(date.today() - timedelta(2)),
            str(date.today() - timedelta(3)),
            str(date.today() - timedelta(4)),
            str(date.today() - timedelta(5)),
            str(date.today() - timedelta(6)),
        ]
        for achievement in person['achievements']:
            for date_obj in key_data:
                if str(achievement['created_on'].date()) == date_obj:
                    key += 1
                    key_data.remove(date_obj)
                    if key == 7:
                        return person['person_name']
                    else:
                        continue
    return 'Сегодня нет победительницы в этой категории'


def create_data():
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
    person = Person.objects.create(
        person_name='Маргарита Михайловна',
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
    achievement = Achievement.objects.create(
        name_achievements='Пустилась в пляс',
        number_of_points=22,
        created_on=date.today() - timedelta(8),
        description='Сдал отчет',
        person=person,
    )
    person.achievements.add(
        achievement,
        through_defaults={'achievement': achievement},
    )
    person = Person.objects.create(
        person_name='Виктория Олеговна',
        language='ru',
    )
    achievement = Achievement.objects.create(
        name_achievements='Пустилась в пляс',
        number_of_points=22,
        created_on=date.today() - timedelta(3),
        description='Сдал отчет',
        person=person,
    )
    person.achievements.add(
        achievement,
        through_defaults={'achievement': achievement},
    )
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
