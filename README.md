# Для запуска проекта нужно:  

1. Сделайте git clone репозитория
2. Запустите Postgres на Docker c командой: docker run --name test_bolid_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
3. Создайте виртуальное окружение внутри проекта python
4. Установите зависимости с командой: pip install -r requirments.txt 
5. Запустите проект с помощью: ./manage.py runserver
6. Пользуйтесь!

Возможно, потребуется сделать superuser-a, для этого использзуйте команду: ./manage.py createsuperuser  и следуйте инструкциям.

Пути: 

1. "event/" - вывод всех событий (get-method)
2. "event/<int:pk>/" - вывод одного события (get-method)
3. "event/create/" - создание события (post-method)
4. "event/<int:pk>/update/" - обновление события (patch-method)
5. "event/<int:pk>/delete/" - удаление записи о событии (delete-method)
6. "event/sensor/" - получение всех датчиков (get-method)
7. "event/sensor/<int:pk>/" - получение датчика по ключу (get-method)
8. "event/sensor/create/" - создание нового датчика (post-method)
9. "event/sensor/<int:pk>/update/" - обновление информации о датчике (patch-method)
10. "event/sensor/<int:pk>/delete/" - удаление записи о датчике (delete-method)
11. "event/create-list/" - Добавление в базу событий из json (post-method)
