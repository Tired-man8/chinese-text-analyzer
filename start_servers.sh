#!/bin/bash

# Start Flask in the background
echo "Starting Flask server..."
python app.py &

# Start Go API
echo "Starting Go API..."
go run chinese_text_api.go