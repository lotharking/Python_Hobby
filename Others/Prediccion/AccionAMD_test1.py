import yfinance as yf

from sklearn.neural_network import MLPRegressor

# Obtenemos los datos de cierre de la empresa AMD
amd = yf.Ticker("AMD")
df = amd.history(period="max")

# Mostramos los últimos 10 datos de cierre
print(df.tail(10))

# Separamos los datos en dos conjuntos: entrenamiento y test
X_train = df.iloc[:-10, :]
X_test = df.iloc[-10:, :]
y_train = df['Close'].iloc[:-10]
y_test = df['Close'].iloc[-10:]

# Creamos el modelo de red neuronal
model = MLPRegressor(hidden_layer_sizes=(50,50,50), max_iter=1000, alpha=0.001, solver='adam', random_state=42)

# Entrenamos el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Hacemos predicciones con el modelo entrenado
predictions = model.predict(X_test)

# Mostramos las predicciones
print(predictions)
