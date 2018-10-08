#!/bin/bash

cd collector.app

source .venv/bin/activate
source ../.env.local
pip3 install -r requirements.txt

export FLASK_APP=runserver.py
flask run --port=5000

