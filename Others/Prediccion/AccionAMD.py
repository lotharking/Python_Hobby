### Usar fuera de apertura del mercado
import yfinance as yf
import openpyxl
import os

# Iterar recursivamente sobre todas las subcarpetas del directorio actual
for root, dirs, files in os.walk("."):
    # Buscar el archivo "predictions.xlsx" en la lista de archivos de la carpeta actual
    if "predictions.xlsx" in files:
        # Si se encuentra el archivo, obtener la ruta completa del archivo
        file_path = os.path.join(root, "predictions.xlsx")
        
        # Abrir el archivo de Excel
        workbook = openpyxl.load_workbook(file_path)
        
        # Procesar el archivo de Excel
        # ...
        
        # Salir del bucle una vez que se ha encontrado el archivo
        break

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

# Seleccionar la primera hoja del libro
worksheet = workbook.active

# Obtener el número de filas en la hoja
row_count = worksheet.max_row

# Añadir una nueva fila al final de la hoja
worksheet.append([row_count+1, predicted_close])

# Guardar los cambios en el archivo
workbook.save("predictions.xlsx")

print("Predicción del precio de cierre del próximo día guardada en el archivo de Excel")

