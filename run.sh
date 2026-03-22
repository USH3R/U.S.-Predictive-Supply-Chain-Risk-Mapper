#!/bin/bash
# run.sh - US Predictive Supply Chain Risk Mapper
# Sets up environment, installs packages, and runs the app

echo "Initializing Python environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install all required packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Run the Dash app
echo "Launching the dashboard..."
python app.py
