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

def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
    
def in_range(value, min_val, max_val) -> bool:
    return value >= min_val and value <= max_val

def invalid_coordinates(path, sep, id_type) -> tuple:
    incorrect = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=sep)
        for row in reader:
            temp_latitude = row["decimalLatitude"]
            temp_longitude = row["decimalLongitude"]
            if is_number(temp_latitude) and is_number(temp_longitude):
                latitude = float(temp_latitude)
                longitude = float(temp_longitude)
                if in_range(latitude, -90, 90) and in_range(longitude, -180, 180):
                    continue
                incorrect.append(row[id_type])
            else:
                incorrect.append(row[id_type])
    return len(incorrect), incorrect


## Ejercicio 3.B
## Un registro geográfico debería tener ambas coordenadas. Escribir una función que detecte registros donde:
## ● exista decimalLatitude pero no decimalLongitude
## ● exista decimalLongitude pero no decimalLatitude.

def coordinate_verification(path, sep, id_type):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=sep)
        for row in reader:
            if (
                row["decimalLatitude"] is not None and row["decimalLatitude"].strip() != ""
            ) and (
                row["decimalLongitude"] is None or row["decimalLongitude"].strip() == ""
            ):
                print(f"The record with id {row[id_type]} has decimalLatitude but not decimalLongitude")

            elif (
                row["decimalLatitude"] is None or row["decimalLatitude"].strip() == ""
            ) and (
                row["decimalLongitude"] is not None and row["decimalLongitude"].strip() != ""
            ):
                print(f"The record with id {row[id_type]} has decimalLongitude but not decimalLatitude")



## Ejercicio 3.C
## Escribir una función que detecte:
## ● fechas con formato inválido
## ● fechas que no puedan interpretarse como fecha
## ● fechas posteriores al año actual
## Puede consultar con su ayudante cómo obtener el formato válido de una fecha. 
## Aplicar esta función de validación a todas los atributos posibles.

def date_verification(date):
    date_str = date_str.replace("/", "-") #convierto a un mismo separador


## Ejercicio 3.D
## Utilizando los “ID” escribir una función que detecte posibles registros duplicados.
## La función deberá indicar:
## ● cuántos registros duplicados existen
## ● qué identificador se repite.

def duplicate_ids(path, sep, id_type):
    id_list = set() # el set usa una tecnica de hashing, mucho mas eficiente que una lista normal
    duplicates = set()
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=sep)
        for row in reader:
            if row[id_type] not in id_list:
                id_list.add(row[id_type])
            else:
                duplicates.add(row[id_type])
    return len(duplicates), list(duplicates)

## Ejercicio 3.E
## El campo countryCode puede tomar solo un conjunto de valores específicos, investigar
## cuáles son y desarrollar una función que detecte valores no permitidos.

## Ejercicio 3.F
## El campo coordinateUncertaintyInMeters representa la incertidumbre en la definición de la coordenada.
## Escribir una función que detecte registros donde:
## ● el valor no sea numérico
## ● el valor sea negativo
## ● el valor sea excesivamente grande (por ejemplo > 100).

def coordinate_uncertainty_validation(path, sep, id_type):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=sep)
        for row in reader:
            if is_number(row["coordinateUncertaintyInMeters"]):
                number = float(row["coordinateUncertaintyInMeters"])
                if in_range(number, 0, 100):
                    continue
                print(f"The record with id {row[id_type]} does not meet the validation")
            else:
                print(f"The record with id {row[id_type]} does not meet the validation")

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