print("Operaciones")
print("S. Suma")
print("R. Resta")
print("M. Multiplicacion")
print("D. Division")
print("A. Salir")

opcion = input("¿Qué opción elige?: ")

while opcion.upper()=="S":
    num1 = float(input("Dame un numero: "))
    num2 = float(input("Dame otro numero: "))
    res = (num1 + num2)
    print("El resultado de la suma es: ", res)
    opcion=input("¿Desea continuar [S/N]?")

while opcion.upper()=="R":
    num1 = float(input("Dame un numero: "))
    num2 = float(input("Dame otro numero: "))
    res = (num1 - num2)
    print("El resultado de la resta es: ", res)
    opcion=input("¿Desea continuar [S/N]?")

while opcion.upper()=="M":
    num1 = float(input("Dame un numero: "))
    num2 = float(input("Dame otro numero: "))
    res = (num1 * num2)
    print("El resultado de la multiplicacion es: ", res)
    opcion=input("¿Desea continuar [S/N]?")

while opcion.upper()=="D":
    num1 = float(input("Dame un numero: "))
    num2 = float(input("Dame otro numero: "))
    res = (num1 / num2)
    print("El resultado de la division es: ", res)
    opcion=input("¿Desea continuar [S/N]?")

while opcion.upper()=="A":
    res = "Saliendo"
    for res in range(1,1):
        print("El programa está ", res)