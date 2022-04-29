from ManejadorRegistro import ManejadorRegistro
from Registro import Registro
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.salir
            }
    def lanzarMenu(self,manejador):
        #Menu opciones
        if type(manejador)==ManejadorRegistro:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para consultar dia y hora de menor y mayor valor.')
                print('-Ingrese 2 para mostrar el promedio mensual de cada hora.')
                print('-Ingrese 3 para mostrar los datos del dia')
                print('-Ingrese 4 para la funcion test.')
                print('-Ingrese 5 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3' or opcion=='4'):
                    ejecutar(manejador)
                else:
                    ejecutar()
    def opcion1(self,manejador):
        manejador.mayorMenor()
    def opcion2(self,manejador):
        manejador.promTemperatura()
    def opcion3(self,manejador):
        num=int(input("Ingrese el numero de dia:")) 
        manejador.buscarDia(num-1)
    def opcion4(self,manejador):
        manejador.funcionTestManejador()
        registro2=Registro()
        registro2.funcionTestRegistro()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')