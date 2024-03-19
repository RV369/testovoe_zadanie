from api.models import Achievement


def list_achievements(person):
    achievements = Achievement.objects.select_related().filter(
        person=person.pk,
    )
    achievement_list, sum_number_of_points = [], 0
    for achievement in achievements:
        achievement_list.append(
            {
                'number_of_points': achievement.number_of_points,
                'created_on': achievement.created_on,
                'person': achievement.person,
            },
        )
        sum_number_of_points += achievement.number_of_points
    return achievement_list, sum_number_of_points


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
            },
        )
    return persons
