from api import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'achievements', views.AchievementViewSet)


urlpatterns = [
    path('count/', views.count_person),
    path('data/', views.data_list),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
