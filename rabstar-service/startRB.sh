#!/bin/sh

export FLASK_APP=rabstartSvc.py

app="flask run --host=107.182.235.108 --port=80"
 
nohup ${app} > ./myrb.log 2>&1 &
