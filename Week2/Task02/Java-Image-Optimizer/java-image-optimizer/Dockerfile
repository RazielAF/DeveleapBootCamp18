FROM openjdk:8u212-jre-alpine3.9

RUN apk update \
&& apk add maven \
&& apk add openjdk8

WORKDIR /app

COPY . .

RUN mvn clean package

ENTRYPOINT java -cp target/deps/pngtastic-1.0.jar -jar target/image-web-optimizer-0.0.2-SNAPSHOT.jar ./in ./out


