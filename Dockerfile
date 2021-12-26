FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR app

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py makemigrations
RUN python manage.py makemigrations animals
RUN python manage.py makemigrations users
#RUN python manage.py migrate

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
