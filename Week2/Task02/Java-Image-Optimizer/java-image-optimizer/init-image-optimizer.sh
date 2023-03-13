#!/bin/bash


docker build -t image-opti .

if [ $# -eq 0 ]
   then
        in_dir="in"
        out_dir="out"
else
        in_dir=$1
        out_dir=$2
fi


docker run -itd -v $(pwd)/${out_dir}:/app/out -v $(pwd)/${in_dir}:/app/in image-opti