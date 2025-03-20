#!/bin/bash

set -e

echo "Installing Python dependencies..."
apt-get update && apt-get install -y python3 python3-pip
pip3 install --upgrade pip
pip3 install -r requirements.txt


echo "Starting Flask server..."
python3 app.py &

echo "Starting Go server..."
./go_server

