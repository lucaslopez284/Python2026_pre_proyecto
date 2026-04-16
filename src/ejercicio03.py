import csv
import datetime

## Ejercicio 3.A
## Los campos decimalLatitude|latitudeDecimal,
## decimalLongitude|longitudeDecimal deben representar coordenadas geográficas válidas.
## Escribir una función que detecte registros donde:
## ● decimalLatitude no esté en el rango [-90, 90]
## ● decimalLongitude no esté en el rango [-180, 180]
## ● alguno de los valores no pueda convertirse a número
## La función debe retornar:
## ● cantidad de registros inválidos
## ● listado de registros incorrectos.

def es_numero(valor: str) -> bool:
    try:
        float(valor)
        return True
    except (ValueError, TypeError):
        return False
    
def en_rango(valor, min, max) -> bool:
    return valor >= min and valor <= max

def coordenadas_invalidas(ruta, separacion, tipo_id) -> tuple:
    incorrectos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo, delimiter=separacion)
        for fila in reader:
            latitud_provisoria = fila["decimalLatitude"]
            longitud_provisoria = fila["decimalLongitude"]
            if es_numero(latitud_provisoria) and es_numero(longitud_provisoria):
                latitud = float(latitud_provisoria)
                longitud = float(longitud_provisoria)
                if en_rango(latitud, -90, 90) and en_rango (longitud, -180, 180):
                    continue
                incorrectos.append(fila[tipo_id])
            else:
                incorrectos.append(fila[tipo_id])
    return len(incorrectos), incorrectos


## Ejercicio 3.B
## Un registro geográfico debería tener ambas coordenadas. Escribir una función que detecte registros donde:
## ● exista decimalLatitude pero no decimalLongitude
## ● exista decimalLongitude pero no decimalLatitude.

def verficacion_coordenadas(ruta, separacion, tipo_id):
    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo, delimiter=separacion)
        for fila in reader:
            if (
                fila["decimalLatitude"] is not None and fila["decimalLatitude"].strip() != ""
            ) and (
                fila["decimalLongitude"] is None or fila["decimalLongitude"].strip() == ""
            ):
                print(f"El registro de id {fila[tipo_id]} tiene decimalLatitude pero no decimalLongitude")

            elif (
                fila["decimalLatitude"] is None or fila["decimalLatitude"].strip() == ""
            ) and (
                fila["decimalLongitude"] is not None and fila["decimalLongitude"].strip() != ""
            ):
                print(f"El registro de id {fila[tipo_id]} tiene decimalLongitude pero no decimalLatitude")



## Ejercicio 3.C
## Escribir una función que detecte:
## ● fechas con formato inválido
## ● fechas que no puedan interpretarse como fecha
## ● fechas posteriores al año actual
## Puede consultar con su ayudante cómo obtener el formato válido de una fecha. 
## Aplicar esta función de validación a todas los atributos posibles.

def verificacion_fecha(fecha):
    fecha_str = fecha_str.replace("/", "-") #convierto a un mismo separador


## Ejercicio 3.D
## Utilizando los “ID” escribir una función que detecte posibles registros duplicados.
## La función deberá indicar:
## ● cuántos registros duplicados existen
## ● qué identificador se repite.

def ids_duplicados(ruta, separacion, tipo_id):
    lista_ids = set() # el set usa una tecnica de hashing, mucho mas eficiente que una lista normal
    duplicados = set()
    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo, delimiter=separacion)
        for fila in reader:
            if fila[tipo_id] not in lista_ids:
                lista_ids.add(fila[tipo_id])
            else:
                duplicados.add(fila[tipo_id])
    return len(duplicados), list(duplicados)

## Ejercicio 3.E
## El campo countryCode puede tomar solo un conjunto de valores específicos, investigar
## cuáles son y desarrollar una función que detecte valores no permitidos.

## Ejercicio 3.F
## El campo coordinateUncertaintyInMeters representa la incertidumbre en la definición de la coordenada.
## Escribir una función que detecte registros donde:
## ● el valor no sea numérico
## ● el valor sea negativo
## ● el valor sea excesivamente grande (por ejemplo > 100).

def validacion_incertidumbre_coordenada(ruta, separacion, tipo_id):
    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo, delimiter=separacion)
        for fila in reader:
            if es_numero(fila["coordinateUncertaintyInMeters"]):
                numero = float(fila["coordinateUncertaintyInMeters"])
                if en_rango(numero, 0, 100):
                    continue
                print(f"El registro de id {fila[tipo_id]} tiene no cumple con la validacion")
            else:
                print(f"El registro de id {fila[tipo_id]} tiene no cumple con la validacion")

## Ejercicio 3.G
## Escribir una función que genere un resumen de calidad del dataset, incluyendo:
## ● cantidad total de registros
## ● registros con coordenadas inválidas
## ● registros con fechas inválidas
## ● registros duplicados
## ● registros con información taxonómica incompleta
## El resultado puede ser un diccionario y un pequeño reporte en texto.

## Ejercicio 3.H
## Establezca cotas de coordenadas para el américa del sur, es decir latitudes y longitudes
## máximas y mínimas que delimitan ocurrencias dentro del territorio (aproximado). A partir de
## estas cotas seteadas como constantes escriba una función que valide los campos de latitud y longitud de cada dataset.

## Ejercicio 3.I
## Escriba una función que agrupe y ejecute todas las validaciones para el campo latitud, y otra independiente para el campo longitud.