FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY . /app
COPY main.py robots.txt ./
RUN chmod +x boot.sh

ENV FLASK_APP main.py

EXPOSE 80
ENTRYPOINT ["./boot.sh"]
