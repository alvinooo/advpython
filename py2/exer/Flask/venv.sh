#!/bin/bash
# venv.sh - create virtualenv and install modules

echo installing virtual environment...
virtualenv venv

echo installing modules...
venv/bin/pip install flask
venv/bin/pip install flask_login
venv/bin/pip install flask_sqlalchemy
venv/bin/pip install sqlalchemy_migrate
venv/bin/pip install flask_wtf
