# mock_data.py - simulated multi-source supply chain data

import pandas as pd

def get_mock_data():
    # Simulate data for 3 vendors
    data = {
        'vendor': ['Vendor A', 'Vendor B', 'Vendor C'],
        'region': ['North', 'South', 'West'],
        'supply_quantity': [100, 200, 150],
        'delivery_delay_days': [2, 5, 1]
    }
    return pd.DataFrame(data)# mock_data.py - Simulated supply chain data
import pandas as pd
import numpy as np

def get_mock_data():
    # Simulate 5 vendors across 3 regions with random metrics
    vendors = ["Vendor A", "Vendor B", "Vendor C", "Vendor D", "Vendor E"]
    regions = ["North", "South", "West"]
    
    data = []
    for v in vendors:
        for r in regions:
            data.append({
                "vendor": v,
                "region": r,
                "metric_1": round(50 + 50 * np.random.rand(), 2),
                "metric_2": round(20 + 30 * np.random.rand(), 2),
                "metric_3": round(5 + 10 * np.random.rand(), 2),
            })
    df = pd.DataFrame(data)
    return df
