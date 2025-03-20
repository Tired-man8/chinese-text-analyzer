#!/bin/bash

echo "Installing Python..."
nix-env -iA nixpkgs.python311  # Install Python 3.11
export PATH=$HOME/.nix-profile/bin:$PATH  # Add Python to PATH

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting Flask server..."
python app.py

echo "Starting Go server..."
go run chinese_text_api.go

