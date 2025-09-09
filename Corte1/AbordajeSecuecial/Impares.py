#El ejercicio vale por una decima / corte 1
while True:
    numero = input("Ingrese un numero: ")
    numero = float(numero)
    numero = int(numero)

    tempResidual = numero%2
    if tempResidual == 0:
        print("El numero", numero, "es par")
    else:
        print("El numero", numero, "es impar")
        
