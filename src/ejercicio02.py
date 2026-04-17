import csv

## Ejercicio 2.A
## Escribir una función que:
## ● Abra el archivo principal del dataset.
## Trabajo Integrador 2026 - Seminario de Lenguajes Opción Python
## ● utilice la librería csv.
## ● imprima las primeras 10 filas del dataset.
## Esto permitirá verificar que el archivo fue abierto correctamente.

def read_dataset_first_ten(path, delimiter):
    file = open(path, "r", encoding="utf-8")
    csv_reader = csv.reader(file, delimiter=delimiter)
    # Imprime las primeraas 10 col
    counter = 0
    for row in csv_reader:
        if counter < 10:
          print(row)
          counter += 1
    file.close()

## Ejercicio 2.B
## Escribir una función que retorne una lista completa de columnas del dataset.

def get_columns(path, delimiter) -> list:
    with open(path, "r", encoding="utf-8") as open_file:
        read_data = csv.reader(open_file, delimiter=delimiter)
        columns = next(read_data)
        return columns
    
## Ejercicio 2.C
## Escribir una función que retorne la posición (índice) de cada columna dentro del archivo.

def return_column_positions(path, delimiter) -> dict:
  file = open(path, "r", encoding="utf-8") 
  reader = csv.reader(file, delimiter=delimiter) 
  positions = {}
  cols = next(reader)
  for index, column in enumerate(cols):
    positions[column] = index
  file.close()
  return positions

## Ejercicio 2.D
## Escribir una función que retorne la cantidad total de registros del dataset.

def total_records(path, delimiter) -> int:
  file = open(path, "r", encoding="utf-8") 
  reader = csv.reader(file, delimiter=delimiter) 
  total_count = 0
  for col in reader: # recorre cada registro
    total_count += 1
  file.close()
  return total_count - 1 

## Ejercicio 2.E
## Escribir una función que retorne las columnas que posean al menos un dato con registro nulo.

def list_null_columns(path, delimiter) -> list:
   result = set()
   with open (path, encoding="utf-8") as file:
      reader = csv.DictReader(file, delimiter=delimiter)
      for row in reader:
         for column, value in row.items():
            if value is None or value.strip() == "":
               result.add(column)
   return list(result)

## Ejercicio 2.F
## Escribir una función que retorne para cada columna el porcentaje de registros nulos.

def null_percentage(path, delimiter) -> dict:
   result = {}
   total_count = total_records(path, delimiter)
   with open (path, encoding="utf-8") as file:
      reader = csv.DictReader(file, delimiter=delimiter)
      for row in reader:
         for column, value in row.items():
            if column not in result:
               result[column] = 0
            if value is None or value.strip() == "":
               result[column] = result[column] + 1
   
   for column in result:
      result[column] = (result[column] / total_count) * 100

   return result

## Ejercicio 2.G
## Escribir una función que, dado el nombre de una columna, retorne la cantidad de valores
## distintos presentes en dicha columna. Si la columna no existe se debe informar de dicha situación

def count_distinct_values(path, delimiter, column_name) -> int:
   result = set()
   with open (path, encoding="utf-8") as file:
      reader = csv.DictReader(file, delimiter=delimiter)
      if column_name not in reader.fieldnames:
            print("La columna no existe")
            return 0
      for row in reader:
         value = row[column_name]
         if value is not None and value.strip() != "":
                result.add(value)
   return len(result)



## Ejercicio 2.H
## Escribir una función que, dado el nombre de una columna, retorne la frecuencia de aparición de cada valor.
## El resultado puede representarse mediante un diccionario:
## {
## "Argentina": 1250,
## "Brazil": 230,
## "Chile": 80
## }

def distinct_values_frequency(path, delimiter, column_name) -> dict:
   result = {}
   with open (path, encoding="utf-8") as file:
      reader = csv.DictReader(file, delimiter=delimiter)
      if column_name not in reader.fieldnames:
            print("La columna no existe")
            return result
      for row in reader:
         value = row[column_name]
         if value is None or value.strip() == "":
            continue
         if value not in result:
               result[value] = 1
         else:
            result[value] = result[value] + 1
   sorted_result = dict(sorted(result.items(), key=lambda value: value[1], reverse=True))
   return sorted_result

## Ejercicio 2.I
## Escribir una función que dada una columna y su tipo retorne lo establecido a continuación
## Los tipos aceptados son:
## ● numeric: menor valor encontrado, mayor valor encontrado, promedio.
## ● coordinate: menor valor encontrado, mayor valor encontrado.
## ● text: cantidad de caracteres del texto más corto encontrado, cantidad de caracteres del texto más largo encontrado.

def column_min_max(path, delimiter, column_name, data_type) -> tuple:
   result = ()
   values_list = []
   with open (path, encoding="utf-8") as file:
      reader = csv.DictReader(file, delimiter=delimiter)
      if column_name not in reader.fieldnames:
            print("La columna no existe")
            return result
      for row in reader:
         value = row[column_name]
         if value is None or value.strip() == "":
             continue
         values_list.append(value)
      match data_type:
         case "numeric":
            numbers = [float(value) for value in values_list]
            average = sum(numbers) / len(numbers)
            return min(numbers), max(numbers), average
         case "coordinate":
            coords = [float(value) for value in values_list]
            return min(coords), max(coords)
         case "text":
            lengths = [len(value) for value in values_list]
            return min(lengths), max(lengths)
         case _:
            return result

## Ejercicio 2.J
## Escribir una función que identifique columnas cuyo contenido sea completamente nulo en todos los registros.

def columns_all_null(path, delimiter) -> list:
   null_columns_info = null_percentage(path, delimiter)
   result = []
   for column, percentage in null_columns_info.items():
      if percentage == 100:
         result.append(column)
   return result