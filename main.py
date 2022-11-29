import pandas as pd
import json

# TODO Crear un archivo llamado analisis_archivo.csv con un tabulador de delimitador

df = pd.read_csv("GLOBANT.csv")

# Crea una lista con el comportamiento de las acciones

# Esta parte añade una columna llamada stock que equivale a la resta de Close - Open
df["stock"] = (df["Close"] - df["Open"])

# Crea una list comprehension con expresiones condicionales
comportamiento = ["Sube" if x > 0 else "Baja" if x < 0 else "Estable" for x in df["stock"]]

# Crea una lista con el punto medio High-low

df["hl_stock"] = (df["High"] - df["Low"]) / 2
high_low = df["hl_stock"].tolist()

# Crea una lista con la fecha

fechas = df["Date"].tolist()

# TODO Crear analisis_archivo.csv

analisis_archivo = pd.DataFrame({"Fecha": fechas,
                                 "Comportamiento de la accion": comportamiento,
                                 "Punto medio HIGH-LOW": high_low})

analisis_archivo.to_csv("analisis_archivo.csv", sep="\t", index=False)


# TODO Crear un archivo llamado detalles.json
# Este JSON tendrá las siguientes llaves:
# ▪ "date_lowest_price" (Guardará una cadena de texto)
# ▪ "lowest_price" (Guardará un número flotante)
# ▪ "date_highest_price" (Guardará una cadena de texto)
# ▪ "highest_price" (Guardará un número flotante)
# ▪ "cantidad_veces_sube" (Guardará un número entero)
# ▪ "cantidad_veces_baja" (Guardará un número entero)
# ▪ "cantidad_veces_estable" (Guardará un número
# entero)

# gets the id of the max/min item
highest_price_index = df["High"].idxmax()
lowest_price_index = df["Low"].idxmin()
# gets highest price
alto_precio = df["High"].max()
# gets lowest price
bajo_precio = df["Low"].min()

# gets the row of the highest price
highest_row = df.iloc[[highest_price_index]]
alto_fecha = highest_row["Date"].to_string(index=False)
# gets the row of the lowest price
lowest_row = df.iloc[[lowest_price_index]]
bajo_fecha = lowest_row["Date"].to_string(index=False)

# veces que sube accediendo a value_counts y su key

veces_sube = analisis_archivo["Comportamiento de la accion"].value_counts().Sube
# veces que baja accediendo a value_counts y su key
veces_baja = analisis_archivo["Comportamiento de la accion"].value_counts().Baja

veces_estable = 0
for x in analisis_archivo["Comportamiento de la accion"]:
    if x == "Estable":
        veces_estable += 1

details = {
    "date_lowest_price": bajo_fecha,
    "lowest_price": float(bajo_precio),
    "date_highest_price": alto_fecha,
    "highest_price": float(alto_precio),
    "cantidad_veces_sube": int(veces_sube),
    "cantidad_veces_baja": int(veces_baja),
    "cantidad_veces_estable": int(veces_estable)
}

# CREATE THE JSON FILE
detalles = json.dumps(details)

with open("detalles.json", "w") as f:
    f.write(detalles)

