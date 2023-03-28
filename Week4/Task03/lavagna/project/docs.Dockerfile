
FROM maven:3.3-jdk-8 

COPY . .

 RUN mvn clean stampo:build

ENTRYPOINT [ "mvn" ,"stampo:serve" ]