FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate
ENV PORT=8000
CMD python ./manage.py runserver 0.0.0.0:$PORT
