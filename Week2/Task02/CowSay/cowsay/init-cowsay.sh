#!/bin/bash

docker build -t nodecowsay:1 .

if [[ "$1" == "" ]]
    then
        PORT=8080
else
        PORT=$1
fi

docker run -d --name cowsay -p 4001:$PORT nodecowsay:1 $PORT