FROM python:3.6-slim

RUN apt-get update

EXPOSE 9000

WORKDIR /target

COPY requirements.txt ./requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/target/docker-entrypoint.sh"]