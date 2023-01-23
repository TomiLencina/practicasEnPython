from functools import reduce

DESCRIPCION_SERVICIO = {
            '0': 'salon',
            '1': 'salon,animacion',
            '2': 'salon,animacion  y comida',
            '3': 'salon,animacion, comida y sorprecita'
        }

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
class ReservaManager:

    def file_to_reserva(self):
        array_reservas = list()
        with open('reservas.csv', 'r') as file:
            for line in file:
                data = line.split(',')
                reserva = Reserva(*data)
                array_reservas.append(reserva)
        return array_reservas


    #01-Mostrar reservas

    def show_reservas(self,lista_reserva):
        for reserva in lista_reserva:
            print(reserva._to_screen_())


    def suma_servicio(self,array_reserva,servicio):
        vector = list()
        for reserva in array_reserva:
            if reserva.get_servicio() == servicio:
                vector.append(reserva.get_monto())
        
        return reduce ((lambda x,y: x+y),vector) if vector else 0


    #03- De todo el array de reservas, agrupar por tipo y mostrar el total del grupo
    def sum_service_montos(self,array_reserva):
        dicc_sumas = dict()
        for i in range(len(array_reserva[0].descripcion_servicio)):
            result = self.suma_servicio(array_reserva,i)
            dicc_sumas[i] = result
            print("El servicio {}:{} tiene una facturacion de: ${}".format(i,DESCRIPCION_SERVICIO[str(i)],result))


        Key_max = max(zip(dicc_sumas.values(),dicc_sumas.keys()))[1]
        print("El servicio con mayor facturacion es: ", DESCRIPCION_SERVICIO[str(Key_max)])   


    #04 - Crear vector
    def crear_vector(self,atributo,condicion,array):
        nuevo_array = list()
        
        for reserva in array:
            print(reserva.__dict__[atributo])
            if reserva.__dict__[atributo] > condicion:
                nuevo_array.append(reserva)
        
        
        return nuevo_array

    def crear_vector_filtrado(self,dicc_filtro,array):
        for filtro in dicc_filtro:
            array = self.crear_vector(filtro,dicc_filtro[filtro],array)
        self.show_reservas(array)

        return array 


dicc_filtro = {
    "edad":5,
    "invitados": 10,

}
reservaM = ReservaManager()


array = reservaM.file_to_reserva()
reservaM.show_reservas(array)
reservaM.sum_service_montos(array)
reservaM.crear_vector("edad",10,array)

print("--------------------------")
reservaM.crear_vector_filtrado(dicc_filtro,array)