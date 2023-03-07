FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

RUN pip install --upgrade pip
# install psycopg2 dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt


RUN mkdir /app
WORKDIR /app

COPY . .

CMD ["python", "/app/docker/docker.py"]