# PITCHIN BACKEND

using django

## HOW TO USE

1. git clone

   `$ git clone`

2. use virtual environment

   - make virtual environment

     `$ virtualenv pitchin`

     or

     `$ python -m virtualenv pitchin`

   - start virtual env

     - if linux

       `$ source pitchin/bin/activate`

     - if Window

       `$ pitchin\Script\activate`

3. install require pakages

   `$ pip install -r requirments.txt`

4. install redis for chatting apps

- if linux

  `$ apt install redis-server`

- if window

  [redis github](https://github.com/microsoftarchive/redis)

  for this pakage => v3.0

- U should service start redis so, check redis server

  `$ sudo systemctl status redis`

5. start django

   - python manage.py makemigrations app

   - python manage.py migrate

   - python manage.py runserver 0.0.0.0:8000 (for debug not service)
