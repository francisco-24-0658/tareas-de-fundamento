def capturar_notas():
  estudiantes = []

  while True:
      nombre = input("Ingrese el nombre del estudiante: ")
      matricula = input("Ingrese la matrícula del estudiante: ")

      notas = []
      for i in range(1, 5):
          while True:
              try:
                  nota = float(input(f"Ingrese la nota {i} del estudiante (0-100): "))
                  if nota < 0 or nota > 100:
                      print("La nota debe estar entre 0 y 100. Intente de nuevo.")
                  else:
                      notas.append(nota)
                      break
              except ValueError:
                  print("Entrada inválida. Por favor, ingrese un número válido.")

      promedio = sum(notas) / len(notas)
      estudiantes.append((nombre, matricula, promedio))

      continuar = input("¿Desea capturar las notas de otro estudiante? (s/n): ").lower()
      if continuar != 's':
          break

  print("\nPromedios de los estudiantes:")
  for estudiante in estudiantes:
      print(f"Nombre: {estudiante[0]}, Matrícula: {estudiante[1]}, Promedio: {estudiante[2]:.2f}")

if __name__ == "__main__":
  capturar_notas()
