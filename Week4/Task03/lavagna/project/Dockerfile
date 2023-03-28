FROM maven:3.3-jdk-8

WORKDIR /app

COPY . .

RUN mvn verify

ENTRYPOINT [ "bash entrypoint.sh" ]
