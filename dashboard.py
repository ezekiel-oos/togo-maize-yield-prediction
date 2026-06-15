import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# --- Chargement des données ---
df = pd.read_csv("FAOSTAT_data_en_6-8-2026.csv")
df_togo = df[["Year", "Value"]]

# --- Entraînement du modèle ---
X = df_togo[["Year"]]
y = df_togo["Value"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- Application Dash ---
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Rendement du Maïs au Togo (1961-2024)",
        style={"textAlign": "center", "color": "#2c6e2e"}
    ),

    html.P(
        "Source : FAOSTAT — Nations Unies",
        style={"textAlign": "center", "color": "gray"}
    ),

    dcc.Graph(id="graphique-rendement"),

    html.Div([
        html.H3("Prédiction du rendement", style={"color": "#2c6e2e"}),
        html.Label("Choisissez une année :"),
        dcc.Slider(
            id="slider-annee",
            min=2025,
            max=2035,
            step=1,
            value=2025,
            marks={i: str(i) for i in range(2025, 2036)},
        ),
        html.Div(id="resultat-prediction", style={
            "fontSize": "20px",
            "marginTop": "20px",
            "padding": "15px",
            "backgroundColor": "#f0f7f0",
            "borderRadius": "10px"
        })
    ], style={"padding": "20px", "margin": "20px"})
])

@app.callback(
    Output("graphique-rendement", "figure"),
    Input("slider-annee", "value")
)
def update_graph(annee):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_togo["Year"],
        y=df_togo["Value"],
        mode="lines",
        name="Rendement réel",
        line=dict(color="green", width=2)
    ))

    annees_futures = list(range(2025, annee + 1))
    predictions = model.predict(
        pd.DataFrame({"Year": annees_futures})
    )

    fig.add_trace(go.Scatter(
        x=annees_futures,
        y=predictions,
        mode="lines+markers",
        name="Prédictions",
        line=dict(color="orange", width=2, dash="dash")
    ))

    fig.update_layout(
        title="Évolution du rendement du maïs au Togo",
        xaxis_title="Année",
        yaxis_title="Rendement (kg/ha)",
        legend=dict(x=0, y=1)
    )

    return fig

@app.callback(
    Output("resultat-prediction", "children"),
    Input("slider-annee", "value")
)
def update_prediction(annee):
    pred = model.predict(pd.DataFrame({"Year": [annee]}))[0]
    return f"Rendement prédit en {annee} : {pred:.1f} kg/ha"

if __name__ == "__main__":
    app.run(debug=True)