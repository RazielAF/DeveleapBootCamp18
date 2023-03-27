#!/bin/bash

npm install 
sleep 1
npm run build
sleep 1
pip install -r requirements.txt
sleep 1
python ./app.py