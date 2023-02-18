# Для запуска проекта нужно:  

1. Сделайте git clone репозитория
2. Запустите Postgres на Docker c командой: docker run --name test_bolid_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
3. Запустите проект с помощью: ./manage.py runserver
4. Пользуйтесь!