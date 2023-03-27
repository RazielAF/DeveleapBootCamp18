FROM alpine:3.15

COPY foodtrucks/project/ /app/

WORKDIR /app/flask-app

RUN apk add --update python2 nodejs npm bash &&\
    python -m ensurepip &&\
    pip install --upgrade pip setuptools

COPY ./init.sh .

RUN chmod 777  ./init.sh

ENTRYPOINT sh -c  ./init.sh
