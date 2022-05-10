FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate
# install psycopg2

ENV PORT=8000
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT