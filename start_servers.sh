#!/bin/bash

echo "Installing Python..."
nix-env -iA nixpkgs.python311  # Install Python 3.11
export PATH=$HOME/.nix-profile/bin:$PATH  # Add Python to PATH

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements.txt

echo "Installing Go..."
curl -LO https://go.dev/dl/go1.20.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.20.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin

echo "Starting Flask server..."
gunicorn -w 4 -b 0.0.0.0:5000 app:app &

echo "Starting Go server..."
go run chinese_text_api.go
./chinese_text_api.go
