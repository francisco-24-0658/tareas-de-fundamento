vocales  = ['a', 'e', 'i', 'o', 'u']
nombre = input('ingrese su nombre')
numer0_vocales = 0
for letra in nombre:
    if letra in vocales:
        numer0_vocales += 1

if numer0_vocales >= 3:
    print('el nombre que ingreso tiene 3 vocales o mas')