numeros = []
menor = ""
mayor = ""
resultado = ""

numeroIngresado = input("Ingrese un número de 4 dígitos: ")

for caracter in numeroIngresado:
    numeros.append(caracter)

while resultado != "6174":
    resultado = ""
    menor = ""
    mayor = ""
    numeros.sort()
    for numero in numeros:
        menor = menor+numero

    numeros.reverse()
    for numero in numeros:
        mayor = mayor + numero

    resultado = str(int(mayor)-int(menor))
    print(f"{mayor} - {menor} = {resultado}")

    numeros.clear()
    for x in resultado:
        numeros.append(x)
