# data.py - US Predictive Supply Chain Risk Mapper
# Provides supply chain data for the dashboard

import pandas as pd

def get_supply_data():
    """
    Returns a simple DataFrame with supply chain data.
    Ready for model.py's predict_risk() function.
    """
    # Example data
    data = {
        'vendor': ['A', 'B', 'C'],
        'region': ['North', 'South', 'West'],
        'delivery_time': [5, 8, 3],
        'cost': [100, 200, 150],
        'other_metric': [0.1, 0.2, 0.3]
    }

    df = pd.DataFrame(data)
    return df
