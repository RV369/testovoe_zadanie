from api.core_processor import (
    achievements_for_7_consecutive_days,
    list_person,
    max_difference_in_achievement_points,
    string_translate,
)
from api.models import Achievement, AchievementPerson, Person
from rest_framework import serializers


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

    def create(self, validated_data):
        person = validated_data.pop('person')
        achievements = Achievement.objects.create(
            **validated_data,
            person=person,
        )
        AchievementPerson.objects.create(
            achievement=achievements,
            person=person,
        )
        return achievements


class AchievementBuiltInSerializer(serializers.ModelSerializer):
    name_achievements = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = (
            'pk',
            'name_achievements',
            'number_of_points',
            'created_on',
            'description',
        )

    def get_name_achievements(self, validated_data):
        name_achievements = validated_data.name_achievements
        if validated_data.person.language != 'ru':
            return string_translate(
                name_achievements,
                validated_data.person.language,
            )
        return name_achievements

    def get_description(self, validated_data):
        description = validated_data.description
        if validated_data.person.language != 'ru':
            return string_translate(
                description,
                validated_data.person.language,
            )
        return description


class PersonSerializer(serializers.ModelSerializer):
    person_name = serializers.SerializerMethodField()
    achievements = AchievementBuiltInSerializer(many=True, required=False)

    class Meta:
        model = Person
        fields = (
            'pk',
            'person_name',
            'language',
            'achievements',
        )

    def get_person_name(self, validated_data):
        person_name = validated_data.person_name
        if validated_data.language != 'ru':
            return string_translate(person_name, validated_data.language)
        return person_name


class PersonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class PersonCountSerializer(serializers.ModelSerializer):
    achievements_max_count = serializers.SerializerMethodField()
    sum_number_of_points = serializers.SerializerMethodField()
    max_difference_in_achievement_points = serializers.SerializerMethodField()
    min_difference_in_achievement_points = serializers.SerializerMethodField()
    achievements_for_7_consecutive_days = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = (
            'achievements_max_count',
            'sum_number_of_points',
            'max_difference_in_achievement_points',
            'min_difference_in_achievement_points',
            'achievements_for_7_consecutive_days',
        )

    def get_achievements_max_count(self, validated_data):
        persons = list_person(validated_data)
        persons.sort(key=lambda x: x.get('achievements_count'))
        if persons == []:
            return 'Отсутствуют данные в базе данных'
        return persons[-1]['person_name']

    def get_sum_number_of_points(self, validated_data):
        persons = list_person(validated_data)
        persons.sort(key=lambda x: x.get('sum_number_of_points'))
        if persons == []:
            return 'Отсутствуют данные в базе данных'
        return persons[-1]['person_name']

    def get_max_difference_in_achievement_points(self, validated_data):
        persons = max_difference_in_achievement_points(
            list_person(validated_data),
        )
        persons.sort(key=lambda x: x.get('number'))
        if persons == []:
            return 'Отсутствуют данные в базе данных'
        return persons[-1]['person_name']

    def get_min_difference_in_achievement_points(self, validated_data):
        persons = max_difference_in_achievement_points(
            list_person(validated_data),
        )
        persons.sort(key=lambda x: x.get('number'))
        if persons == []:
            return 'Отсутствуют данные в базе данных'
        return persons[0]['person_name']

    def get_achievements_for_7_consecutive_days(self, validated_data):
        return achievements_for_7_consecutive_days(list_person(validated_data))
