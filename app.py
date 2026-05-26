import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Ler dados
df = pd.read_csv("vendas.csv")

# Criar app
app = Dash(__name__)

# Layout
app.layout = html.Div(style={
    "fontFamily": "Arial",
    "padding": "30px",
    "backgroundColor": "#f4f4f4"
}, children=[

    html.H1(
        "Dashboard de Vendas",
        style={"textAlign": "center"}
    ),

    html.Div([
        html.Label("Escolha o tipo de gráfico:"),

        dcc.Dropdown(
            id="tipo-grafico",
            options=[
                {"label": "Gráfico de Barras", "value": "bar"},
                {"label": "Gráfico de Pizza", "value": "pie"},
                {"label": "Gráfico de Linha", "value": "line"},
            ],
            value="bar",
            clearable=False,
            style={"width": "300px"}
        ),
    ]),

    dcc.Graph(id="grafico-vendas")
])

# Interatividade
@app.callback(
    Output("grafico-vendas", "figure"),
    Input("tipo-grafico", "value")
)

def atualizar_grafico(tipo):

    if tipo == "bar":
        fig = px.bar(
            df,
            x="produto",
            y="vendas",
            text="vendas",
            title="Vendas por Produto"
        )

    elif tipo == "pie":
        fig = px.pie(
            df,
            names="produto",
            values="vendas",
            title="Participação nas Vendas"
        )

    else:
        fig = px.line(
            df,
            x="produto",
            y="vendas",
            markers=True,
            title="Evolução de Vendas"
        )

    # Remove informações extras ao passar mouse
    fig.update_traces(
        hovertemplate=None,
        hoverinfo="skip"
    )

    # Melhor visual
    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig

# Rodar app
if __name__ == "__main__":
    app.run(debug=True)