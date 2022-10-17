#En química, el pH es una escala utilizada para especificar la acidez o basicidad de un líquido.
#Cree un programa ph_levels.py que compruebe si un nivel de pH es básico, ácido o neutro.

def ph():
    ok = True
    while ok:
            valor = int(input("ingrese el valor del ph: "))
            if valor < 0: 
                print("Incorrecto, los valores de PH van desde 0 a 14...")
                print("Intenta nuevamente...")
                continue
            elif valor > 14:
                print("Incorrecto, los valores de PH van desde 0 a 14...")
                print("Intenta nuevamente...")
                continue
            ok = False
    if valor > 7:
        print("El ph es basico")
    elif valor < 7:
        print("El ph es acido")
    else:
        print("El ph es neutro")

ph()
