# FROM maven:3.3-jdk-8

# WORKDIR /lavagna

# COPY . .

# RUN mvn com.mycila:license-maven-plugin:format
# RUN mvn verify

# ENV DB_DIALECT MYSQL
# ENV DB_URL jdbc:mysql://mysql:3306/lavagna?useSSL=false
# ENV DB_USER root
# ENV DB_PASS 12345
# ENV SPRING_PROFILE dev

# ENTRYPOINT [ "bash", "entrypoint.sh" ]

# EXPOSE 8080

FROM maven:3.3-jdk-8 as builder
WORKDIR /app
COPY . .
RUN mvn com.mycila:license-maven-plugin:format
RUN mvn verify

FROM openjdk:8-jre-alpine
WORKDIR /app
COPY --from=builder /app/target ./target/
COPY ./entrypoint.sh .

ENV DB_DIALECT MYSQL
ENV DB_URL jdbc:mysql://mysql:3306/lavagna?useSSL=false
ENV DB_USER root
ENV DB_PASS 12345
ENV SPRING_PROFILE dev

ENTRYPOINT [ "sh", "entrypoint.sh"]
