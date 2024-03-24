from api.models import Achievement, AchievementPerson, Person
from rest_framework import serializers
from api.core_processor import string_translate


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
        # fields = '__all__'
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
                name_achievements, validated_data.person.language,
            )
        return name_achievements

    def get_description(self, validated_data):
        description = validated_data.description
        if validated_data.person.language != 'ru':
            return string_translate(
                description, validated_data.person.language,
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
        max_count = Person.objects.raw(
            'SELECT d.person_id, a.id, COUNT(*) as c '
            'FROM api_person as a '
            'INNER JOIN api_achievementperson as d '
            'ON d.[person_id] = a.[id]'
            'GROUP BY person_name '
            'ORDER BY c DESC LIMIT 1;',
        )
        for person in max_count:
            person.person_name
        try:
            return str(person.person_name)
        except UnboundLocalError as e:
            return 'Отсутствуют данные: ' + str(e)

    def get_sum_number_of_points(self, validated_data):
        number_of_points = Person.objects.raw(
            'SELECT d.person_id, a.person_name, a.id, '
            'MAX(number_of_points) as c'
            'FROM api_person as a'
            'INNER JOIN api_achievement as d'
            'ON d.[person_id]=a.[id]'
            'GROUP BY person_name '
            'ORDER BY c DESC LIMIT 1;',
        )
        for person in number_of_points:
            person.person_name
        try:
            return str(person.person_name)
        except UnboundLocalError as e:
            return 'Отсутствуют данные: ' + str(e)

    def get_max_difference_in_achievement_points(self, validated_data):
        difference_number_of_points = Person.objects.raw(
            'SELECT d.person_id, a.person_name, a.id,'
            'MAX(number_of_points) - MIN(number_of_points) as c'
            'FROM api_person as a'
            'INNER JOIN api_achievement as d'
            'on d.[person_id]=a.[id]'
            'GROUP BY person_name'
            'ORDER BY c DESC LIMIT 1;',
        )
        for person in difference_number_of_points:
            person.person_name
        try:
            return str(person.person_name)
        except UnboundLocalError as e:
            return 'Отсутствуют данные: ' + str(e)

    def get_min_difference_in_achievement_points(self, validated_data):
        difference_number_of_points = Person.objects.raw(
            'SELECT d.person_id, a.person_name, a.id,'
            'MAX(number_of_points) - MIN(number_of_points) as c'
            'FROM api_person as a'
            'INNER JOIN api_achievement as d'
            'on d.[person_id]=a.[id]'
            'GROUP BY person_name'
            'ORDER BY c LIMIT 1;',
        )
        for person in difference_number_of_points:
            person.person_name
        try:
            return str(person.person_name)
        except UnboundLocalError as e:
            return 'Отсутствуют данные: ' + str(e)

    def get_achievements_for_7_consecutive_days(self, validated_data):
        difference_number_of_points = Person.objects.raw(
            'SELECT a.person_name, a.id, d.created_on, COUNT(*) as c'
            'FROM api_person as a '
            'INNER JOIN api_achievement as d'
            'ON d.[person_id]=a.[id]'
            'WHERE d.created_on >= CURRENT_DATE - 7'
            'AND d.created_on >= CURRENT_DATE - 1'
            'AND d.created_on >= CURRENT_DATE - 2'
            'AND d.created_on >= CURRENT_DATE - 3'
            'AND d.created_on >= CURRENT_DATE - 4'
            'AND d.created_on >= CURRENT_DATE - 5'
            'AND d.created_on >= CURRENT_DATE - 6'
            'GROUP BY person_name'
            'ORDER BY c DESC LIMIT 1;',
        )
        for person in difference_number_of_points:
            person.person_name
        try:
            return str(person.person_name)
        except UnboundLocalError as e:
            return 'Отсутствуют данные: ' + str(e)
