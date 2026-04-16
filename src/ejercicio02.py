import csv

## Ejercicio 2.A
## Escribir una función que:
## ● Abra el archivo principal del dataset.
## Trabajo Integrador 2026 - Seminario de Lenguajes Opción Python
## ● utilice la librería csv.
## ● imprima las primeras 10 filas del dataset.
## Esto permitirá verificar que el archivo fue abierto correctamente.

def leer_dataset_diez_primeras(ruta, separacion):
    file = open(ruta, "r", encoding="utf-8")
    csv_reader = csv.reader(file, delimiter=separacion)
    # Imprime las primeraas 10 col
    i = 0
    for col in csv_reader:
        if i < 10:
          print(col)
          i += 1
    file.close()

## Ejercicio 2.B
## Escribir una función que retorne una lista completa de columnas del dataset.

def obtener_columnas(ruta, separacion) -> list:
    with open(ruta, "r", encoding="utf-8") as abrir_arch:
        leer_data = csv.reader(abrir_arch, delimiter=separacion)
        columnas = next(leer_data)
        return columnas
    
## Ejercicio 2.C
## Escribir una función que retorne la posición (índice) de cada columna dentro del archivo.

def retornar_pos_col(ruta, separacion)-> dict:
  archivo = open(ruta, "r", encoding="utf-8") 
  leer_data = csv.reader(archivo, delimiter=separacion) 
  posiciones = {}
  cols = next(leer_data)
    # enumerate retorna = indice (se guarda en i) y valor (se guarda en col)
  for indice, columna in enumerate(cols):
    posiciones[columna] = indice
  archivo.close()
  return posiciones

## Ejercicio 2.D
## Escribir una función que retorne la cantidad total de registros del dataset.

def total_registros(ruta, separacion) -> int:
  archivo = open(ruta, "r", encoding="utf-8") 
  leer_data = csv.reader(archivo, delimiter=separacion) 
  cantidad_registros = 0
  for col in leer_data: # recorre cada registro
    cantidad_registros += 1
  archivo.close()
  return cantidad_registros - 1 

## Ejercicio 2.E
## Escribir una función que retorne las columnas que posean al menos un dato con registro nulo.

def lista_de_nulos(ruta, separacion) -> list:
   resultado = set()
   with open (ruta, encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo, delimiter=separacion)
      for fila in reader:
         for columna, valor in fila.items():
            if valor is None or valor.strip() == "":
               resultado.add(columna)
   return list(resultado)

## Ejercicio 2.F
## Escribir una función que retorne para cada columna el porcentaje de registros nulos.

def porcentaje_de_nulos(ruta, separacion) -> dict:
   resultado = {}
   cant_registros = total_registros(ruta, separacion)
   with open (ruta, encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo, delimiter=separacion)
      for fila in reader:
         for columna, valor in fila.items():
            if columna not in resultado:
               resultado[columna] = 0
            if valor is None or valor.strip() == "":
               resultado[columna] = resultado[columna] + 1
   
   for columna in resultado:
      resultado[columna] = (resultado[columna] / cant_registros) * 100

   return resultado

## Ejercicio 2.G
## Escribir una función que, dado el nombre de una columna, retorne la cantidad de valores
## distintos presentes en dicha columna. Si la columna no existe se debe informar de dicha situación

def cantidad_valores_distintos(ruta, separacion, nombre_columna) -> int:
   resultado = set()
   with open (ruta, encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo, delimiter=separacion)
      if nombre_columna not in reader.fieldnames:
            print("La columna no existe")
            return 0
      for fila in reader:
         valor = fila[nombre_columna]
         if valor is not None and valor.strip() != "":
                resultado.add(valor)
   return len(resultado)



## Ejercicio 2.H
## Escribir una función que, dado el nombre de una columna, retorne la frecuencia de aparición de cada valor.
## El resultado puede representarse mediante un diccionario:
## {
## "Argentina": 1250,
## "Brazil": 230,
## "Chile": 80
## }

def frecuencia_valores_distintos(ruta, separacion, nombre_columna) -> dict:
   resultado = {}
   with open (ruta, encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo, delimiter=separacion)
      if nombre_columna not in reader.fieldnames:
            print("La columna no existe")
            return resultado
      for fila in reader:
         valor = fila[nombre_columna]
         if valor is None or valor.strip() == "":
            continue
         if valor not in resultado:
               resultado[valor] = 1
         else:
            resultado[valor] = resultado[valor] + 1
   resultado_ordenado=dict(sorted(resultado.items(), key=lambda valor: valor[1], reverse=True))
   return resultado_ordenado

## Ejercicio 2.I
## Escribir una función que dada una columna y su tipo retorne lo establecido a continuación
## Los tipos aceptados son:
## ● numeric: menor valor encontrado, mayor valor encontrado, promedio.
## ● coordinate: menor valor encontrado, mayor valor encontrado.
## ● text: cantidad de caracteres del texto más corto encontrado, cantidad de caracteres del texto más largo encontrado.

def minimo_maximo_columna(ruta, separacion, nombre_columna, tipo) -> tuple:
   resultado = ()
   lista = []
   with open (ruta, encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo, delimiter=separacion)
      if nombre_columna not in reader.fieldnames:
            print("La columna no existe")
            return resultado
      for fila in reader:
         valor = fila[nombre_columna]
         if valor is None or valor.strip() == "":
             continue
         lista.append(valor)
      match tipo:
         case "numeric":
            numeros = [float(valor) for valor in lista]
            promedio = sum(numeros) / len(numeros)
            return min(numeros), max(numeros), promedio
         case "coordinate":
            return min(lista), max(lista)
         case "text":
            longitudes = [len(valor) for valor in lista]
            return min(longitudes), max(longitudes)
         case _:
            return resultado

## Ejercicio 2.J
## Escribir una función que identifique columnas cuyo contenido sea completamente nulo en todos los registros.

def columnas_con_todo_nulo(ruta, separacion) -> list:
   columnas_info_nulos = porcentaje_de_nulos(ruta, separacion)
   resultado = []
   for columna, porcentaje in columnas_info_nulos.items():
      if porcentaje == 100:
         resultado.append(columna)
   return resultado
    

      