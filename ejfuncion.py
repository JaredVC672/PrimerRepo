# Escribir un programa que pida al usuario un texto y un número entero.
# Mandar a imprimir en pantalla, el texto repetido las veces indicados por el número.
# NOTA: Hacer el programa usando una función.

#Declarar la función

def repetir(texto, numero):
    texto +='\n'
    print(texto*numero)

# Escribir el codigo para usar la funcion

t = input("Ingresa un texto: ")
n = int(input("Ingresa un numero: "))

repetir(t,n)