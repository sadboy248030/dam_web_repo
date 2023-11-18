import datetime

# Obtener la fecha y hora actuales
now = datetime.datetime.now()

# Formatear la fecha y hora como una cadena
formatted_datetime = now.strftime("%d-%m-%Y %H:%M:%S")

# Tu nombre
nombre = "Alfonso"

# Imprimir el nombre y la fecha y hora
print(f"{nombre}, la fecha y hora actual son: {formatted_datetime}")

