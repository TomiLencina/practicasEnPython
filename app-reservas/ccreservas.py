from cv2 import reduce


class Reserva:
    def __init__(self,numero,nombre,edad,servicio,invitados,monto):
        self.numero = int(numero)
        self.nombre = nombre.strip()
        self.edad = int(edad)
        self.servicio = int(servicio)
        self.invitados = int(invitados)
        self.monto = int(monto)
        self.descripcion_servicio = {
            '0': 'salon',
            '1': 'salon,animacion',
            '2': 'salon,animacion  y comida',
            '3': 'salon,animacion, comida y sorprecita'
        }

    def get_numero(self):
            return self.numero

    def get_nombre(self):
            return self.nombre

    def get_edad(self):
            return self.edad

    def get_servicio(self):
            return self.servicio

    def get_invitados(self):
            return self.invitados

    def get_monto(self):
            return self.monto
        
    def __str__(self):
            return "{},{},{},{},{},{}".format(self.numero, self.nombre, self.edad,self.servicio, self.invitados,self.monto)

    def _to_screen_(self):
            return (f"Numero de reserva: {self.numero} | Nombre {self.nombre} | Edad: {self.edad} | Servicio {self.servicio} | Invitados: {self.invitados} | Monto {self.monto}")


#Abrir el archivo
#Cargar los datos del archivo a una lista de tipo reserva

def file_to_reserva():
    array_reservas = list()
    with open('reservas.csv', 'r') as file:
        for line in file:
            data = line.split(',')
            reserva = Reserva(*data)
            array_reservas.append(reserva)
    return array_reservas

def show_reservas(lista_reserva):
    for reserva in lista_reserva:
        print(reserva._to_screen_())


def suma_servicio(array_reserva,servicio):
    vector = list()
    for reserva in array_reserva:
        if reserva.get_servicio() == servicio:
            vector.append(reserva.get_monto())
    
    return reduce((lambda x,y: x+y),vector,"") if vector else 0



def sum_service_montos(array_reserva):
    for i in range(len(array_reserva[0].descripcion_servicio)):
        print(suma_servicio(array_reserva,i))

array = file_to_reserva()
show_reservas(array)
sum_service_montos(array)