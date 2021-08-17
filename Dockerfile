FROM python:3.8.11-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y install sudo

#RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
#USER docker

RUN apt-get update; apt-get clean

RUN mkdir /ui_testrunner
WORKDIR /ui_testrunner
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system
COPY . /ui_testrunner
