# Import libraries

import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from sklearn.linear_model import LinearRegression

from prefect import task, Flow
from prefect.tasks.secrets import PrefectSecret

# Extract of data
@task
def extract(ticker):
    # Obtener el precio de cierre de la acción de AMD en el último mes
    history = ticker.history(period="1mo")

# Transform
@task
def transform(data):
    # Seleccionar la columna de "Close" como la variable dependiente (y)
    y = data["Close"]

    # Seleccionar las columnas de "Volume" y "Market Index" como variables independientes (X)
    X = data[["Volume", "Market Index"]]
    # Crear un modelo de regresión lineal
    model = LinearRegression()

    # Entrenar el modelo con los datos de entrenamiento
    model.fit(X, y)
    # Hacer predicciones con el modelo entrenado
    predictions = model.predict([[100000, 20000]])
    print(predictions)

# Load
@task
def load(tablon, today, credentials):
    pass

# Flow
with Flow("ETL caso") as flow:
    # Enviroment variables
    ticker = yf.Ticker("AMD")
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    data = pd.read_csv("./Others/Prediccion/dataframe.csv")

    raw_dfs = extract(ticker)
    # tablon = transform(data)
    # load(tablon, today, credentials)

flow.run()