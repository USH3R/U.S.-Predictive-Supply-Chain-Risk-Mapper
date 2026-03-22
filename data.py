# data.py
# Modular data loading for US Predictive Supply Chain Risk Mapper

import pandas as pd
from sqlalchemy import create_engine
from neo4j import GraphDatabase
import requests

# ----------------------------
# SQL Data
# ----------------------------
def load_sql_data(connection_string, query):
    """
    Load data from SQL database.
    """
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df

# ----------------------------
# Neo4j Graph Data
# ----------------------------
def load_neo4j_data(uri, user, password, cypher_query):
    """
    Load data from Neo4j graph database.
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        result = session.run(cypher_query)
        data = [record.data() for record in result]
    driver.close()
    return pd.DataFrame(data)

# ----------------------------
# API Data
# ----------------------------
def load_api_data(url, params=None):
    """
    Load JSON data from an API.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    return pd.DataFrame(response.json())

# ----------------------------
# Sample placeholder data
# ----------------------------
def load_sample_data():
    """
    Return a small sample dataset for dashboard testing.
    """
    data = pd.DataFrame({
        'vendor': ['Vendor A', 'Vendor B', 'Vendor C'],
        'risk_score': [0.2, 0.5, 0.8],
        'criticality': [3, 2, 5],
        'week': [1, 1, 1]
    })
    return data
