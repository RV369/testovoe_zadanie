from api import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('', views.achievement_list, name='index'),
    path('persons/', views.person_list, name='persons'),
    path('person/<int:pk>/', views.person, name='person'),
    path('count/', views.count_person, name='count'),
]
