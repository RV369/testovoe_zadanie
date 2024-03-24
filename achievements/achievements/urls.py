from django.contrib import admin
from django.urls import path, include
from api.views import (
    PersonViewSet,
    AchievementViewSet,
    count_person,
    data_list,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'achievements', AchievementViewSet)


urlpatterns = [
    path('count/', count_person),
    path('data/', data_list),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
