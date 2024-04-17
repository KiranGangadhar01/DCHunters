FROM python:2.7

ADD ./DCHunter /app
WORKDIR /app/

CMD python manage.py
