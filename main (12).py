def operar_texto(texto):
  # 1) Retornar todo el texto en mayúsculas
  mayusculas = texto.upper()

  # 2) Retornar todo el texto en minúsculas
  minusculas = texto.lower()

  # 3) Retornar los dos primeros caracteres del texto
  dos_primeros = texto[:2]

  # 4) Retornar los dos últimos caracteres del texto
  dos_ultimos = texto[-2:]

  # 5) Retornar la cantidad de veces que se repite el último caracter
  if len(texto) > 0:
      ultimo_caracter = texto[-1]
      cuenta_ultimo = texto.count(ultimo_caracter)
  else:
      cuenta_ultimo = 0

  # 6) Retornar el texto invertido
  invertido = texto[::-1]

  # Retornar resultados en un diccionario
  resultados = {
      'mayusculas': mayusculas,
      'minusculas': minusculas,
      'dos_primeros': dos_primeros,
      'dos_ultimos': dos_ultimos,
      'cuenta_ultimo': cuenta_ultimo,
      'invertido': invertido
  }

  return resultados

# Ejemplo de uso
texto = input("Ingrese un texto: ")
resultados = operar_texto(texto)

# Imprimir resultados
for operacion, resultado in resultados.items():
  print(f"{operacion}: {resultado}")
