from ManejadorRegistro import ManejadorRegistro
from Registro import Registro
from Menu import Menu
if __name__=='__main__':
    canDias=int(input("Ingrese la cantidad de dias "))
    if canDias<1:
        print("no valido")
    else:
        manejador=ManejadorRegistro()
        manejador.agregarDias(canDias)
        manejador.cargarArchivo() 
        menu=Menu()
        menu.lanzarMenu(manejador)

    

