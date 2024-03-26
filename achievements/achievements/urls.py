from api.views import (
    AchievementViewSet,
    PersonViewSet,
    count_person,
    data_list,
)
from django.contrib import admin
from django.urls import include, path
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
