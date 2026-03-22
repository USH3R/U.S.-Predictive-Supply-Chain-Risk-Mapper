# model.py - US Predictive Supply Chain Risk Mapper
# Modular predictive model functions

import pandas as pd
import numpy as np

def predict_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder function for risk prediction.
    Accepts a DataFrame and returns the same DataFrame
    with added 'risk_score' column.
    """
    df = df.copy()
    # Simple mock risk score: random between 0 and 1
    df['risk_score'] = np.random.rand(len(df))
    return df
