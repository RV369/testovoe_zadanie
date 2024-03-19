from django.contrib import admin

from .models import Achievement, AchievementPerson, Person


class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'description',
        'created_on',
        'number_of_points',
        'person',
    )


admin.site.register(Achievement)
admin.site.register(Person)
admin.site.register(AchievementPerson)
