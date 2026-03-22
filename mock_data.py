# mock_data.py - Simulated supply chain data
import pandas as pd

def get_mock_data():
    # Simulate 5 vendors across 3 regions
    vendors = ["Vendor A", "Vendor B", "Vendor C", "Vendor D", "Vendor E"]
    regions = ["North", "South", "West"]
    
    # Generate 15 rows with random metrics
    data = []
    for v in vendors:
        for r in regions:
            data.append({
                "vendor": v,
                "region": r,
                "metric_1": round(50 + 50 * pd.np.random.rand(), 2),
                "metric_2": round(20 + 30 * pd.np.random.rand(), 2),
                "metric_3": round(5 + 10 * pd.np.random.rand(), 2),
            })
    df = pd.DataFrame(data)
    return df
