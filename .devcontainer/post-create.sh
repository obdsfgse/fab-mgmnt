#!/bin/bash
set -e

# Create and activate Python virtual environment
python3 -m venv .venv

# Install Python dependencies
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "✓ Development environment setup complete!"
echo "✓ Virtual environment created and dependencies installed"
