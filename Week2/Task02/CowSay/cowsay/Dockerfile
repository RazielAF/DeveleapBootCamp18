FROM node:lts-alpine3.17

WORKDIR /app

COPY ./src/package*.json .

RUN npm install 

COPY . .

RUN chmod 777 ./entry-point.sh

RUN apk add --no-cache bash

WORKDIR /app/src

ENTRYPOINT [ "/bin/bash","/app/entry-point.sh"]


