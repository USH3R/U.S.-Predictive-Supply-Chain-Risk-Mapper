# data.py
# Placeholder for loading and managing supply chain data

import pandas as pd

def load_sample_data():
    """
    Returns a small sample dataset.
    In the future, this function will connect to SQL/Neo4j or other sources.
    """
    data = pd.DataFrame({
        'vendor': ['Vendor A', 'Vendor B', 'Vendor C'],
        'risk_score': [0.2, 0.5, 0.8],
        'criticality': [3, 2, 5]
    })
    return data
