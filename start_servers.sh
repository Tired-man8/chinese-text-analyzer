#!/bin/bash

set -e

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting Flask server..."
python app.py &

echo "Starting Go server..."
go run chinese_text_api.go

