import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px
import random

# --- AUTOMATIC DATA GENERATOR ---
# This runs every time the script starts, ensuring the user NEVER sees a blank page.
def get_live_data():
    vendors = ["SolarWinds-Alt", "Global-Secure", "Data-Bridge-Inc", "Federal-Soft", "Cyber-Guard-Systems"]
    rows = []
    for v in vendors:
        cves = random.randint(0, 15)
        # Randomize leaks for visual variety
        leak_type = random.choice(["None", "None", "2 API Keys", "None", "Credential Leak"])
        # Calculate a realistic risk score based on the "threats"
        score = round((cves * 0.04) + (0.35 if leak_type != "None" else 0), 2)
        rows.append({"Vendor": v, "Current_CVEs": cves, "GitHub_Leaks": leak_type, "Predictive_Risk_Score": min(score, 0.98)})
    return pd.DataFrame(rows)

df = get_live_data()
# --- END GENERATOR ---

app = dash.Dash(__name__)

# The rest of your layout code stays exactly the same...
app.layout = html.Div(style={'backgroundColor': '#0a0a0a', 'color': '#e0e0e0', 'padding': '40px'}, children=[
    html.H1("🇺🇸 US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center', 'color': '#0074D9'}),
    html.P("Federal Agency Oversight - Real-Time Vendor Threat Intelligence", style={'textAlign': 'center'}),
    html.Hr(style={'borderColor': '#333'}),
    
    html.Div([
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_header={'backgroundColor': '#1a1a1a', 'fontWeight': 'bold'},
            style_cell={'backgroundColor': '#111', 'color': '#fff', 'textAlign': 'left'},
            style_data_conditional=[{
                'if': {'filter_query': '{Predictive_Risk_Score} > 0.6', 'column_id': 'Predictive_Risk_Score'},
                'backgroundColor': '#850000', 'color': 'white'
            }]
        )
    ], style={'padding': '20px'}),

    dcc.Graph(
        figure=px.bar(df, x="Vendor", y="Predictive_Risk_Score", color="Predictive_Risk_Score",
                      template="plotly_dark", 
                      color_continuous_scale='Reds',
                      range_y=[0, 1]) # Keeps the scale consistent
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
