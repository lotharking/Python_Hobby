# Import libraries

import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from sklearn.linear_model import LinearRegression
import csv
import os

from prefect import task, Flow

# Extract of data
@task
def extract(ticker,file_path):
    # Obtener el precio de cierre de la acción de AMD en el último mes
    history = ticker.history(period="1mo")

    # Abrir el archivo CSV en modo escritura
    with open(file_path, 'w', newline='') as csvfile:
        # Crear un objeto writer para escribir en el archivo CSV
        writer = csv.writer(csvfile)
        # Añadir una fila con los encabezados
        writer.writerow(["Fecha", "Close", "Volume", "Market Index"])
        
        # Recorrer el DataFrame con los precios de cierre
        for index, row in history.iterrows():
            # Añadir una fila al archivo CSV con la fecha en formato "YYYY-MM-DD" y el precio de cierre
            writer.writerow([index.strftime("%Y-%m-%d"), row["Close"], row["Volume"], row["Open"]])

# Transform
@task
def transform(file_path):    
    data = pd.read_csv(file_path)
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

    file_path = "./Others/Prediccion/dataframe.csv"

    # Comprobar si el archivo existe
    if os.path.exists(file_path):
        os.remove(file_path)

    raw_dfs = extract(ticker, file_path)
    tablon = transform(file_path)
    # load(tablon, today, credentials)

flow.run()