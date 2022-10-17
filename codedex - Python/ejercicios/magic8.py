#---Magic 8 Ball ---
# es un juguete de oficina popular y un juguete para niños inventado en la década de 1940 para adivinar y buscar consejos. 🎱
#Cree un programa magic8.py que pueda responder cualquier pregunta de Sí o No con una fortuna/consejo diferente cada vez que se ejecute.

import random

num = random.randint(1, 9)

def magic(num):
    if num == 1:
        print("Si, definitivamente")
    elif num == 2:
        print("Eso seguramente es así")
    elif num == 3:
        print("Pregunta de nuevo mas tarde.")
    elif num == 4:
        print("Pregunta confusa, pregunta de nuevo.")
    elif num == 5:
        print("Mejor no decirte ahora.")
    elif num == 6:
        print("Mis fuentes dicen que no.")
    elif num == 7:
        print("Las perspectivas no son tan buenas")
    elif num == 8:
        print("Muy dudoso.")
    elif num == 9:
        print("Sin dudas.")

pregunta = str(input("Ingresa tu pregunta: "))
respuesta = magic(num)

