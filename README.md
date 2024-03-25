# testovoe_zadanie
Прежде всего необходимо сделать миграции внутри запущенного контейнера >>
sudo docker container ls
docker compose exec <Номер контейнера> python manage.py migrate

Создать суперюзера >>
docker compose exec <Номер контейнера> python manage.py createsuperuser

Собираем и копируем статические файлы >>
docker compose exec <Номер контейнера> python manage.py collectstatic
docker compose exec <Номер контейнера> cp -r /app/collected_static/. /app/static/

Администрирование Django >>
http://127.0.0.1:8000/admin/

GET запрос на эндпоинт заполняет базу тестовыми данными >>
http://127.0.0.1:8000/api/data/

DELETE запрос на эндпоинт удаляет загруженные данные из базы >>
http://127.0.0.1:8000/api/data/

GET запрос на эндпоинт вернет списов объектов из базы >>
http://127.0.0.1:8000/api/person/

GET запрос выводит информацию о пользователе по id в адресе запроса, если указан язык 'en' система переводит имя персоны, наименования достижений и описания достижений на аглийский язык (на другие языки тоже переводит) >>
http://127.0.0.1:8000/api/person/1/

POST запрос на эндпоинт создаёт новую персону >>
## {
##    "person_name": "Мария Ивановна",
##    "language": "ru"
## }
http://127.0.0.1:8000/api/person/

POST запрос на эндпоинт создаёт новую достижение >>
## {
##    "name_achievements": "Сдал отчёт",
##    "description": "Сдал отчет",
##    "number_of_points": 1,
##    "created_on": "2024-03-16T13:06:41Z",
##    "person": 1
## }
http://127.0.0.1:8000/api/achievements/

GET запрос выводит все достижения имеющиеся в базе >>
http://127.0.0.1:8000/api/achievements/

GET запрос выводит статистические данные >>
http://127.0.0.1:8000/api/count/

◦ пользователь с максимальным количеством достижений >>
achievements_max_count

◦ пользователь с максимальным количеством очков достижений >>
sum_number_of_points

◦ пользователи с максимальной разностью очков достижений >>
max_difference_in_achievement_points

◦ пользователи с минимальной разностью очков достижений >>
min_difference_in_achievement_points

◦ пользователи, у которых достижения выдавались 7 дней подряд >>
achievements_for_7_consecutive_days

## {
##    "achievements_max_count": "Анна Ивановна",
##    "sum_number_of_points": "Маргарита Олеговна",
##    "max_difference_in_achievement_points": "Анна Ивановна",
##    "min_difference_in_achievement_points": "Виктория Олеговна",
##    "achievements_for_7_consecutive_days": "Анна Ивановна"
## }
