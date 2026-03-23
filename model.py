# model.py - US Predictive Supply Chain Risk Mapper
# Contains the predictive model logic

import pandas as pd
import numpy as np

def predict_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a 'risk_score' column to the DataFrame.
    Uses a simple mock formula for demonstration.
    """
    df = df.copy()
    
    # Avoid division by zero
    max_cost = df['cost'].max() if not df['cost'].empty else 1
    max_delivery = df['delivery_time'].max() if not df['delivery_time'].empty else 1
    
    # Mock risk score calculation (0 to 1)
    df['risk_score'] = (
        0.5 * (df['cost'] / max_cost) +
        0.5 * (df['delivery_time'] / max_delivery)
    )
    
    # Clip to 0-1 just in case
    df['risk_score'] = df['risk_score'].clip(0, 1)
    
    return df
