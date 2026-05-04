import os
os.system("cls")
from random import randint
try:
    while True:
        
        num1 = int(input("Ingrese el rango mínimo:\n"))
        num2 = int(input("Ingrese el rango máximo:\n"))

        numero = randint(num1,num2)
        if numero % 2 == 1:
            if (numero + 1) in range(num1,num2) :
                numero_final  = numero + 1
            elif (numero + 1) not in range(num1,num2):
                numero_final = numero - 1


        intento1 = int(input("Intente adivinar:\n"))
        if intento1 > numero_final:
            print("El número es menor")
        elif intento1 < numero_final:
            print("El número es mayor")
        else:
            print("Felicidades, acertaste a la primera.")
            break

        intento2 = int(input("Intente adivinar nuevamente:\n"))
        if intento2 > numero_final:
            print("El número es menor")
            print("Te daré una pista:")
            if (intento2 - numero_final) > (intento1 - numero_final):
                print(f"El número está más cerca de {intento1} que de {intento2}")
            elif (intento2 - numero_final) < (intento1 - numero_final):
                print(f"El número está más cerca de {intento2} que de {intento1}")
        elif intento2 < numero_final:
            print("El número es mayor")
            print("Te daré una pista:")
            if (intento2 - numero_final) > (intento1 - numero_final):
                print(f"El número está más cerca de {intento1} que de {intento2}")
            elif (intento2 - numero_final) < (intento1 - numero_final):
                print(f"El número está más cerca de {intento2} que de {intento1}")
        else:
            print("Felicidades, acertaste en el segundo intento.")
            break
        intento3 = int(input("Última oportunidad para adivinar:\n"))
        if intento3 == numero_final:
            print("Felicidades, acertaste en el tercer intento.")
            break
        else:
            print("Has perdido.")
            print(f"El número era:\n{numero_final}")
            break

except:
    print("El valor debe ser númerico")
    
