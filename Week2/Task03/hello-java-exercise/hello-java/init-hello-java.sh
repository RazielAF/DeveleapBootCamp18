#!/bin/bash

echo "Stage 1- Creating Image..."
sleep 3
docker build -t multistage-java .
sleep 4
echo "Stage 2- Building final image..."
echo "Stage 3- Running the container"
docker run -d --name multistage-java-hello multistage-java
echo "Showing result..."
sleep 2
docker logs multistage-java-hello 
