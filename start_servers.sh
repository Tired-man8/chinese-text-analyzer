#!/bin/bash

echo "Installing Python dependencies..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Starting Flask server..."
python app.py

echo "Starting Go server..."
go run chinese_text_api.go

