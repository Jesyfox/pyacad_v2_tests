# pyacad_v2_tests

need to be installed:

1: redis-server

2: postgresql

to start:

1: `python3 -m venv venv`

2: `. venv/bin/activate`

3: `pip install -r requrements.txt`

4: `sudo su - postgres`

5: `psql`

6: `CREATE DATABASE tests_db;`

7: `CREATE USER tester WITH PASSWORD '123456';`

8: `GRANT ALL PRIVILEGES ON DATABASE tests_db TO tester;`

9: `./manage.py makemigrations`

10: `./manage.py migrate`

11: `celery -A app_tests worker --loglevel=info` on first terminal

12 `./manage.py runserver` on second terminal