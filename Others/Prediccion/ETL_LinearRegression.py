# Import libraries

import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import csv
import os

from prefect import task, Flow

# Extract of data
@task
def extract(ticker,file_path):
    # Obtener el precio de cierre de la acción de AMD en el último mes
    history = ticker.history(period="max")

    # Abrir el archivo CSV en modo escritura
    with open(file_path, 'w', newline='') as csvfile:
        # Crear un objeto writer para escribir en el archivo CSV
        writer = csv.writer(csvfile)
        # Añadir una fila con los encabezados
        writer.writerow(["Fecha", "Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"])
        
        # Recorrer el DataFrame con los precios de cierre
        for index, row in history.iterrows():
            # Añadir una fila al archivo CSV con la fecha en formato "YYYY-MM-DD" y el precio de cierre
            writer.writerow([index.strftime("%Y-%m-%d"), row["Open"], row["High"], row["Low"], row["Close"], row["Volume"], row["Dividends"], row["Stock Splits"]])

# Transform
@task
def transform(file_path):    
    data = pd.read_csv(file_path, header=0, names=["Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"])

    X_train = data.iloc[:-10, :]
    X_test = data.iloc[-10:, :]
    y_train = data['Close'].iloc[:-10]
    y_test = data['Close'].iloc[-10:]

    # Creamos el modelo de red neuronal
    model = MLPRegressor(hidden_layer_sizes=(50,50,50), max_iter=1000, alpha=0.001, solver='adam', random_state=42)

    # Entrenamos el modelo con los datos de entrenamiento
    model.fit(X_train, y_train)

    # Hacemos predicciones con el modelo entrenado
    predictions = model.predict(X_test)

    # Mostramos las predicciones
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