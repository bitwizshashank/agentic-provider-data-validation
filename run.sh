#!/bin/bash
# Activate venv (optional). Create venv: python -m venv venv
# On Linux/Mac:
# source venv/bin/activate
# pip install -r requirements.txt
# Then run:
export FLASK_APP=app.py
flask run --port=5001
# Or: python app.py
