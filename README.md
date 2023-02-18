# Для запуска проекта нужно:  

1. Сделайте git clone репозитория
2. Запустите Postgres на Docker c командой: docker run --name test_bolid_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
3. Создайте виртуальное окружение внутри проекта python
4. Установите зависимости с командой: pip install -r requirments.txt 
5. Запустите проект с помощью: ./manage.py runserver
6. Пользуйтесь!

Возможно, потребуется сделать superuser-a, для этого использзуйте команду: ./manage.py createsuperuser  и следуйте инструкциям.