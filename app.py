# app.py
# US Predictive Supply Chain Risk Mapper - Modular version

import dash
from dash import html, dcc, Input, Output
import plotly.express as px

from data import load_sample_data
from model import predict_risk

# Load data and apply predictive model
data = load_sample_data()
data = predict_risk(data)

# Create Dash app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center'}),
    
    html.P("Interactive dashboard to explore predictive supply chain risks."),
    
    # Dropdown to select vendor
    html.Label("Select Vendor:"),
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': v, 'value': v} for v in data['vendor']],
        value=data['vendor'][0]
    ),
    
    # Graph for predicted risk
    dcc.Graph(id='risk-graph'),
    
    # Table for vendor details
    html.Div(id='vendor-details')
])

# Callbacks
@app.callback(
    Output('risk-graph', 'figure'),
    Output('vendor-details', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_vendor):
    filtered = data[data['vendor'] == selected_vendor]
    
    fig = px.bar(
        filtered,
        x='vendor',
        y='predicted_risk',
        title=f'Predicted Risk for {selected_vendor}'
    )
    
    details = html.Table([
        html.Tr([html.Th("Vendor"), html.Th("Risk Score"), html.Th("Criticality")]),
        html.Tr([html.Td(filtered['vendor'].values[0]),
                 html.Td(filtered['risk_score'].values[0]),
                 html.Td(filtered['criticality'].values[0])])
    ])
    
    return fig, details

# Run
if __name__ == '__main__':
    app.run(debug=True)
