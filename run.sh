#!/bin/bash
# US Predictive Supply Chain Risk Mapper - Entry Point

echo "-------------------------------------------------------"
echo "🇺🇸 INITIALIZING FEDERAL RISK MAPPER"
echo "-------------------------------------------------------"

# 1. Create Virtual Environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created."
fi

# 2. Activate Environment
source venv/bin/activate

# 3. Install Dependencies
echo "📦 Installing Python libraries (Dash, SQL, Scikit-Learn)..."
pip install -r requirements.txt

# 4. Launch Application
echo "🚀 Dashboard launching at http://127.0.0.1:8050"
python app.py
