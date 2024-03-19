from api.core_processor import list_person
from api.models import Achievement, AchievementPerson, Person
from rest_framework import serializers


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

    def create(self, validated_data):
        person = validated_data.pop('person')
        achievements = Achievement.objects.create(
            **validated_data, person=person,
        )
        AchievementPerson.objects.create(
            achievement=achievements, person=person,
        )
        return achievements


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonCountSerializer(serializers.ModelSerializer):
    achievements_max_count = serializers.SerializerMethodField()
    sum_number_of_points = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = (
            'achievements_max_count',
            'sum_number_of_points',
        )

    def get_achievements_max_count(self, validated_data):
        persons = list_person(validated_data)
        persons.sort(key=lambda x: x.get('achievements_count'))
        return persons[-1]['person_name']

    def get_sum_number_of_points(self, validated_data):
        persons = list_person(validated_data)
        persons.sort(key=lambda x: x.get('sum_number_of_points'))
        print(persons)
        return persons[-1]['person_name']
