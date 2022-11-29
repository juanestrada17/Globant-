import pandas, json

def solucion():
    df = pandas.read_csv("GLOBANT.csv")

    df["stock"] = (df["Close"] - df["Open"])
    comportamiento = ["SUBE" if x > 0 else "BAJA" if x < 0 else "ESTABLE" for x in df["stock"]]
    df["hl_stock"] = (df["High"] - df["Low"]) / 2
    high_low = df["hl_stock"].tolist()
    fechas = df["Date"].tolist()

    analisis_archivo = pandas.DataFrame({"Fecha": fechas,
                                         "Comportamiento de la accion": comportamiento,
                                         "Punto medio HIGH-LOW": high_low})

    analisis_archivo.to_csv("analisis_archivo.csv", sep="\t", index=False)

    highest_price_index = df["High"].idxmax()
    lowest_price_index = df["Low"].idxmin()

    alto_precio = df["High"].max()

    bajo_precio = df["Low"].min()

    highest_row = df.iloc[[highest_price_index]]
    alto_fecha = highest_row["Date"].to_string(index=False)

    lowest_row = df.iloc[[lowest_price_index]]
    bajo_fecha = lowest_row["Date"].to_string(index=False)

    veces_sube = analisis_archivo["Comportamiento de la accion"].value_counts().SUBE
    veces_baja = analisis_archivo["Comportamiento de la accion"].value_counts().BAJA

    veces_estable = 0
    for x in analisis_archivo["Comportamiento de la accion"]:
        if x == "ESTABLE":
            veces_estable += 1

# El replace quita el espacio en blanco con 0 espacios
    details = {
        "date_lowest_price": str(bajo_fecha).replace(" ", ""),
        "lowest_price": float(bajo_precio),
        "date_highest_price": str(alto_fecha).replace(" ", ""),
        "highest_price": float(alto_precio),
        "cantidad_veces_sube": int(veces_sube),
        "cantidad_veces_baja": int(veces_baja),
        "cantidad_veces_estable": int(veces_estable)
    }

    # CREATE THE JSON FILE
    detalles = json.dumps(details)

    with open("detalles.json", "w") as f:
        f.write(detalles)

solucion()