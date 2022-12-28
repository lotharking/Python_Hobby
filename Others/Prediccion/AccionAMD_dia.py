import yfinance as yf

# Obtener información de la acción de AMD
ticker = yf.Ticker("AMD")

# Obtener el precio de cierre de la acción de AMD en el día de hoy
history = ticker.history(interval="1d")
closing_price = history["Close"][0]

print("El precio de cierre de la acción de AMD del día de hoy es", closing_price)
