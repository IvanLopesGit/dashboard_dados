from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import pandas as pd

# Dataset
# https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

df = pd.read_csv("data/kc_house_data.csv")

titulos_top = df['price'].value_counts().sort_values(ascending=False).head(7)
lista_empregos = titulos_top.index

# (2) achar os cinco empregos mais populares


app = Dash(__name__)

# Definir o layout do dashboard aqui!!!!

app.layout = html.Div([
    html.H1("House Sales in King County, USA",
            className='title'),
    dcc.Dropdown(options=lista_empregos,
                 value=lista_empregos[0],
                 id='dropdown_emprego'),
    html.Hr(),
    dcc.Graph(id='figura1'),

])

# definir a callback que define o titulo do emprego


@app.callback(
    Output('figura1', 'figure'),
    # Output('figura2', 'figure'),
    Input('dropdown_emprego', 'value'),
    # Input('tipo-grafico', 'value'),
)
def teste(value_emprego):
    df1 = df[df['price'] == value_emprego]
    fig1 = px.box(x=df['bedrooms'],
                  y=df['price'],
                  labels=dict(x='quartos', y='preço'),
                  title='Preço por quarto')
    fig1.show()

    return fig1


if __name__ == '__main__':
    app.run_server(debug=True)
