#!/bin/bash

virtualenv -p python3 ./collector.app/.venv
source ./collector.app/.venv/bin/activate

pip3 install -r ./collector.app/requirements.txt

