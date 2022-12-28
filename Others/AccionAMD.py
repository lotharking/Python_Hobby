#### Probar mañana

# import yfinance as yf

# # Obtener información de la acción de AMD
# ticker = yf.Ticker("AMD")
# info = ticker.info

# # Verificar si la clave "regularMarketPrice" existe en el diccionario info
# # y si su valor es distinto de None
# if "regularMarketPrice" in info and info["regularMarketPrice"] is not None:
#     # Obtener el precio de cierre de la acción de AMD en el último mes
#     history = ticker.history(period="1mo")
#     closing_prices = history["Close"]

#     # Calcular el promedio del movimiento del precio de cierre en el último mes
#     movement_average = sum(closing_prices) / len(closing_prices)

#     # Predecir el precio de cierre del próximo día en base al promedio del movimiento del último mes
#     predicted_close = info["regularMarketPrice"] + movement_average

#     print("Predicción del precio de cierre del próximo día:", predicted_close)
# else:
#     print("No se pudo obtener el precio de cierre del último mes")

### Usar fuera de apertura del mercado
import yfinance as yf

# Obtener información de la acción de AMD
ticker = yf.Ticker("AMD")

# Obtener el precio de cierre de la acción de AMD en el último mes
history = ticker.history(period="1mo")
closing_prices = history["Close"]

# Calcular el promedio del movimiento del precio de cierre en el último mes
movement_average = sum(closing_prices) / len(closing_prices)

# Predecir el precio de cierre del próximo día en base al promedio del movimiento del último mes
# y al precio de cierre del último día
predicted_close = closing_prices[-1] + movement_average

print("Predicción del precio de cierre del próximo día:", predicted_close)
