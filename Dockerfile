# syntax=docker/dockerfile:1
FROM python:3.10.5-slim-bullseye

RUN mkdir wd
WORKDIR wd

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./

CMD python3 app.py