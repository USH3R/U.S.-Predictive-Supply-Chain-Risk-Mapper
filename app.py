# app.py
# US Predictive Supply Chain Risk Mapper - Base Dashboard
# Minimal working version for hackathon demo

import dash
from dash import html, dcc

# Create the Dash app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Define the layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center'}),
    html.P("This is a base dashboard. Additional components will display predictive supply chain risk."),
    
    # Example placeholder graph
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Vendor Risk'},
            ],
            'layout': {
                'title': 'Example Supply Chain Risk Visualization'
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
