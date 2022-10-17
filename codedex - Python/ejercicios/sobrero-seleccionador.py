#El Sombrero Seleccionador es un sombrero parlante mágico en el Colegio Hogwarts de Magia y Hechicería. El sombrero decide a cuál de las cuatro "Casas" va cada estudiante de primer año

def casas(casa):
    if casa == "grifindor":
        1
    ravenclaw = []
    hufflepuff = []
    slytherin = []

def sombrero():
    ok = False
    while not ok:
        print("Te gusta el amanecer o el atardecer?")
        rta = int(input("Ingrese su respuesta: "))
        if rta > 2:
            print("intenta de nuevo")
            continue
        elif rta == 1:
                gryffindor.append(1)
                ravenclaw.append(1)
        else:
            hufflepuff.append(1)
            slytherin.append(1)