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
    history = ticker.history(period="1mo")

    # Abrir el archivo CSV en modo escritura
    with open(file_path, 'w', newline='') as csvfile:
        # Crear un objeto writer para escribir en el archivo CSV
        writer = csv.writer(csvfile)
        # Añadir una fila con los encabezados
        writer.writerow(["Fecha", "Close", "Volume", "Open", "High", "Low", "Stock Splits"])
        
        # Recorrer el DataFrame con los precios de cierre
        for index, row in history.iterrows():
            # Añadir una fila al archivo CSV con la fecha en formato "YYYY-MM-DD" y el precio de cierre
            writer.writerow([index.strftime("%Y-%m-%d"), row["Close"], row["Volume"], row["Open"], row["High"], row["Low"], row["Stock Splits"]])

# Transform
@task
def transform(file_path):    
    data = pd.read_csv(file_path, header=0, names=["Open", "High", "Low", "Close", "Volume"])
    
    X = data[["Open", "High", "Low", "Close", "Volume"]]
    y = data["Close"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    nn = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)

    nn.fit(X_train, y_train)

    predictions = nn.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    print(f"Mean squared error: {mse:.2f}")
    print("el valor es " + str(predictions))

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