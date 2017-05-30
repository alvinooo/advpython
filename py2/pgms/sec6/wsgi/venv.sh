#!/bin/bash
# venv.sh - create virtualenv and install modules

echo installing virtual environment...
virtualenv venv

echo installing modules...
venv/bin/pip install requests
