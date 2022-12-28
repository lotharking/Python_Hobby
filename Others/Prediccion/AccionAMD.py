import yfinance as yf
import openpyxl
import os
import datetime

# Iterar recursivamente sobre todas las subcarpetas del directorio actual
for root, dirs, files in os.walk("."):
    # Buscar el archivo "predictions.xlsx" en la lista de archivos de la carpeta actual
    if "predictions.xlsx" in files:
        # Si se encuentra el archivo, obtener la ruta completa del archivo
        file_path = os.path.join(root, "predictions.xlsx")
        
        # Abrir el archivo de Excel
        workbook = openpyxl.load_workbook(file_path)
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

# Obtener la fecha de mañana en formato "dd-mm-yyyy"
tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
# Obtener la fecha de hoy en formato "dd-mm-yyyy"
today = datetime.datetime.today().strftime("%d-%m-%Y")

# Seleccionar la primera hoja del libro
worksheet = workbook.active

# Obtener el número de filas en la hoja
row_count = worksheet.max_row

# Validar la columna de nombre real
if worksheet.cell(1, 1).value != "Número de fila":
    # Si la columna de nombre real está vacía, añadir encabezados a la primera fila
    worksheet.append(["Número de fila", "Fecha", "Predicción del precio de cierre"])

# Añadir una nueva fila al final de la hoja
worksheet.append([row_count+1, tomorrow, predicted_close])

# Guardar los cambios en el archivo
workbook.save(file_path)

print("Predicción del precio de cierre del próximo día guardada en el archivo de Excel")