#!/bin/bash

 
if [[ "$1" == "" ]]
    then
        PORT=8080
else
       export PORT=$1
fi

npm start



