#Cree un programa grades.py que verifique si una calificación está por encima o por debajo de 55.

nombre = input("Ingrese su nombre: ")
nota = int(input("ingrese su nota: "))

if nota > 55:
    print("Aprobaste {}".format(nombre))
else:
    print("Desaprobaste {}".format(nombre))