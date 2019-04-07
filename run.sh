#!/bin/bash

method=$1
key=$2

if [ "$method" = "get" ]
then
    if [ $# -lt 2 ]
    then
        echo "usage: sh web.sh get <key>"
        exit 1
    fi
curl -X GET localhost:5000/get/${key}

elif [ "$method" = "put" ]
then
    if [ $# -lt 3 ]
    then
        echo "usage: sh web.sh put <key> '<value>' (use quotes if there are any spaces in the value)"
        exit 1
    fi
value=$3
curl -X POST localhost:5000/put -d "{\"key\":\"${key}\", \"value\":\"${value}\"}"
fi