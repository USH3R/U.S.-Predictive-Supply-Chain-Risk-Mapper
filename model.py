# model.py - US Predictive Supply Chain Risk Mapper
# Provides a modular interface for predicting supply chain risk

import pandas as pd
import numpy as np

def predict_risk(df):
    """
    Add a 'risk_score' column to the DataFrame.
    Mock predictive model: combines delivery_days and cost.
    
    df: pandas DataFrame with columns 'vendor', 'region', 'delivery_days', 'cost'
    Returns: DataFrame with additional 'risk_score' column
    """
    df = df.copy()
    
    # Normalize delivery_days and cost
    max_days = df['delivery_days'].max() if not df['delivery_days'].empty else 1
    max_cost = df['cost'].max() if not df['cost'].empty else 1
    
    df['norm_days'] = df['delivery_days'] / max_days
    df['norm_cost'] = df['cost'] / max_cost
    
    # Mock risk_score: weighted combination
    df['risk_score'] = 0.6 * df['norm_days'] + 0.4 * df['norm_cost']
    
    # Clip to 0-1 range
    df['risk_score'] = df['risk_score'].clip(0, 1)
    
    # Drop intermediate normalization columns
    df.drop(columns=['norm_days', 'norm_cost'], inplace=True)
    
    return df
