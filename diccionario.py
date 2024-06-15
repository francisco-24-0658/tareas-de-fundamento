# 3.Acceder y modificar elementos: Utiliza índices para acceder a elementos específicos en listas, tuplas o diccionarios. También puedes modificar los valores de los elementos si es necesario.

# Persona

perfil_persona = { "nombre": "Juan", "edad": 30, "ciudad": "Madrid", "profesion": "Ingeniero"}

# Acceder a un valor
nombre = perfil_persona["nombre"]
print(nombre)

edad = perfil_persona["edad"]

ciudad = perfil_persona["ciudad"]

profesion = perfil_persona["profesion"]

print("Me llamo " + nombre + " tengo " + str(edad) + " años, vivo en " + ciudad + " y soy " + profesion)

# Modificar un valor

perfil_persona["profesion"] = "Programador"
perfil_persona["edad"] = 23

print("Nueva edad: " + str(perfil_persona["edad"]))
print("Nueva Profesion: " + perfil_persona["profesion"])