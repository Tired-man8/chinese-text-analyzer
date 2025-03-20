#!/bin/bash

# Start Flask in the background
echo "Starting Flask server..."
# python app.py &
gunicorn -w 4 -b 0.0.0.0:5000 app:app &
# Start Go API
# echo "Starting Go API..."
go run chinese_text_api.go
