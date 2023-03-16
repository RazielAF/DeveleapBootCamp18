FROM maven:3.3-jdk-8 AS compile

WORKDIR /app

COPY . .

RUN mvn verify

FROM openjdk:8-jre-alpine

WORKDIR /app

COPY --from=compile /app/target /app

ENTRYPOINT java -jar hello-java.jar



