from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

LEN_STRING = 200


class Person(models.Model):
    person_name = models.CharField(max_length=LEN_STRING, unique=True)
    language = models.CharField(max_length=LEN_STRING)
    achievements = models.ManyToManyField(
        'Achievement',
        related_name='achievements_person',
        through='AchievementPerson',
    )

    def __str__(self):
        return f'{self.pk} {self.person_name}'


class Achievement(models.Model):
    name = models.CharField(max_length=LEN_STRING)
    number_of_points = models.IntegerField()
    description = models.TextField(max_length=LEN_STRING)
    created_on = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(
        Person, related_name='person', on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.pk} {self.name}'


class AchievementPerson(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} {self.achievement} {self.person}'
