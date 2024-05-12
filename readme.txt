Как создать Django-проект

Создайте корневую директорию проекта.

В корневой директории проекта создайте виртуальное окружение, используя команду:

Windows:        python -m venv venv 

Активируйте виртуальное окружение командой:

Windows:        source venv/Scripts/activate;

pip install -r requirements.txt	

python -m pip install --upgrade pip


Создайте Django-проект в папке виртуального окружения:

                django-admin startproject название_проекта.
				
				python manage.py migrate

Как создать приложение в Django-проекте
Находясь в папке Django-проекта, выполните команду:

                python manage.py startapp имя_приложения

Как зарегистрировать Django-приложение
Добавьте в список INSTALLED_APPS в файле settings.py класс конфига приложения из файла apps.py :
название_проекта/settings.py

                INSTALLED_APPS = [
                    'имя_приложения.apps.ИмяПриложенияConfig',
                    ...
                    ]

Как запустить Django-проект
Находясь в папке Django-проекта, выполните команду:

                python manage.py runserver

Загрузка фикстур

				python manage.py loaddata db.json 

Секрет мудрого учителя Хо — знания и шпаргалки.