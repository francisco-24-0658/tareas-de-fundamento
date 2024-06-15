# Operaciones matemáticas: Utiliza listas o tuplas para realizar operaciones matemáticas en conjuntos de datos. Por ejemplo, puedes sumar los elementos de una lista, obtener el producto de una tupla o calcular la media de una lista de números.

tupla_numero = (10, 20, 30,40, 50, 60, 70, 80, 90, 100, 110,120,130,140,150,160,170,180,190,200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320,320, 330, 340, 350, 360, 370, 380, 390, 400, 410)

# Buscar la media aritmetica

suma_acc = 0

for valor in tupla_numero:
    suma_acc = suma_acc + valor

media = (suma_acc / len(tupla_numero))

print("Suma total: " + str(suma_acc))
print("Media aritmetica: " + str( round(media, 2) ))