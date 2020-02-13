print "Practica 1"
print "Tarea 1.2"
print "Punto 1"
name=['Luis','Edgar','Ariel','Israel']
print (name[0])
print (name[1])
print (name[2])
print (name[3])
print "Punto 2"
print (name[0]+" se feliz")
print (name[1]+" se la come")
print (name[2]+" tambien se la come")
print (name[3]+" toma agua")
print "Punto 3"
lista_deseo=['terminar mi carrera','tocar el piano','tener un pecesito','tener una novia','saber cocinar','que este programa jale','pasar programacion','llegar temprano a mis clases','que me jale el proximo programa','que se me ocurran mas deseos','una botella de agua','que me pase el profe','ser mas aplicado','aprender ingles','varo']
l=(input("ponga el numero de desea ver del 0-14 "))
print ("Deseo "+ lista_deseo[l])
m=(input("ponga el numero de desea ver del 0-14 "))
print ("Deseo "+ lista_deseo[m])
n=(input("ponga el numero de desea ver del 0-14 "))
print ("Deseo "+ lista_deseo[n])
print "Tarea 3.4"
def make_shirt(size, message):
    print("Que sea de talla," + size + " mi playera.")
    print('Que diga, "' + message + '"')
make_shirt('Grande', 'dame unos tacos')
def make_shirt(size='Grande', message='I love Python!'):
    print("Que sea talla" + size + " mi playera.")
    print('Que diga, "' + message + '"')
make_shirt()
make_shirt(size='Mediana')
make_shirt('Chica', 'chetos.')
"""Ciudades y paises"""
def describe_city(ciudad, pais='Mexico'):
    """Describe a city."""
    mensaje = ciudad.title() + " esta en " + pais + "."
    print(mensaje)
describe_city('edomex')
describe_city('madrid', 'España')
describe_city('morelos')
"""Clases, Tarea 4.2"""
print('Restaurante')
class Restaurant():
    def __init__(self, nombre, tipo_Restaurante):
        """Initialize the restaurant."""
        self.nombre = nombre.title()
        self.tipo_Restaurante = tipo_Restaurante
    def describe_restaurant(self):
        msg = self.nombre + " el mejor servio de " + self.tipo_Restaurante + "."
        print(msg)
    def open_restaurant(self):
        msg = self.nombre + " abierto ahora, adelante!"
        print(msg)
restaurant = Restaurant('Mario´s', 'pizza')
print(restaurant.nombre)
print(restaurant.tipo_Restaurante)
restaurant.describe_restaurant()
restaurant.open_restaurant()
""""3 Restaurantes"""
print( )
print('3 Restaurantes')
class Restaurant():
    def __init__(self, nombre, tipo_Restaurante):
        self.nombre = nombre.title()
        self.tipo_Restaurante = tipo_Restaurante
    def describe_restaurant(self):
        msg = self.nombre + " del mejor servicio de " + self.tipo_Restaurante + "."
        print(msg)
    def open_restaurant(self):
        msg = self.nombre + " abierto ahora, pase!"
        print(msg)
Elperro_loco = Restaurant('EL perro loco', 'tacos')
Elperro_loco.describe_restaurant()
Elperro_loco.open_restaurant()
Dona_pelos = Restaurant("Doña pelos", 'quesadillas')
Dona_pelos.describe_restaurant()
Dona_pelos.open_restaurant()
Programando = Restaurant('Programando', 'Hamburguesas')
Programando.describe_restaurant()
Programando.open_restaurant()
"""Usuarios"""
print('10 usuarios')
class User():
    def __init__(self, first_name, last_name, username, correo, localidad):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.correo = correo
        self.localidad = localidad.title()
    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Correo: " + self.correo)
        print("  Localidad: " + self.localidad)
    def greet_user(self):
        print("Bienvenido, " + self.username + "!")
Goku = User('Diego', 'Arvisu', 'bolitocha', 'Goku@programacion.com', 'nose ')
Goku.describe_user()
Goku.greet_user()
Sixto = User('Maya', 'trejo', 'mayita', 'mayita@matlab.com', 'bambu')
Sixto.describe_user()
Sixto.greet_user()
Luisito = User('Luisito', 'Aguilar', 'Mijo', 'tenem@programacion.com', 'cdmx')
Luisito.describe_user()
Luisito.greet_user()
Berto = User('Diana', 'Martinez', 'Trapo', 'BMW@programacion.com', 'titan')
Berto.describe_user()
Berto.greet_user()
Danielsito = User('Daniel', 'Uribe', 'Rifle', 'Rifle@programacion.com', 'bambu')
Danielsito.describe_user()
Danielsito.greet_user()
Brian = User('kevin', 'desconocido', 'mr. tec', 'Br@programacion.com', 'Merced')
Brian.describe_user()
Brian.greet_user()
Jerry = User('Jerry', 'Darwin', 'Nigga', 'Darwin@programacion.com', 'campo')
Jerry.describe_user()
Jerry.greet_user()
Negrete = User('Negrete', 'Uribe', 'Nutria', 'Nu@programacion.com', 'Ecatepec')
Negrete.describe_user()
Negrete.greet_user()
Sireno = User('Lamba', 'Bega', 'Sandia', 'migajas@programacion.com', 'neza')
Sireno.describe_user()
Sireno.greet_user()
 