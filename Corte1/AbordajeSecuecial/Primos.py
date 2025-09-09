#El ejercicio vale 1 decima / corte 1

while True:
    numero = input('Ingrese un numero: ')
    numero = int(numero)
    divisores = 0
    a = 1

    for i in range(2,numero - 1):
        if numero%i == 0:
            divisores = divisores + 1

    if divisores == 0:
        print("El numero", numero, "es primo")
    else:
       print("El numero", numero, "no es primo")

    print("\n")
    print('si quiere continuar precione 1')
    a = input()
    a = int(a)

    if a != 1:
        break

print("Gracias por usar el codigo XD")
