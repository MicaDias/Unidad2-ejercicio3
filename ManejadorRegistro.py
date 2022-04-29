import csv 
from Registro import Registro

class ManejadorRegistro:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarDias(self,dias):
        for i in range(dias):
            self.__lista.append([])
    def agregarHoras(self,dia):
        for i in range(24):
            self.__lista[dia].append(None)
    def cargarRegistro(self,registro,dia,hora):
        if type(registro)==Registro:
            if len(self.__lista[dia])==0:
                self.agregarHoras(dia)
            self.__lista[dia][hora]=registro
        else:
            print("No se pudo agregar el registro")
            
    def cargarArchivo(self):
        archivo=open("archivo.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                
                temperatura=int(fila[2])
                humedad=int(fila[3])
                presion=int(fila[4])
                registro=Registro(temperatura,humedad,presion)
                self.cargarRegistro(registro,int(fila[0])-1,int(fila[1]))
        archivo.close()
        
    def buscarDia(self,num):
        if num<=len(self.__lista):
            if len(self.__lista[num])==0:
                print("No se registraron datos")
            else:
                print("{0:^10} {1:^10} {2:^10} {3:^10}".format('Hora','Temperatura','Humedad','Presion'))
                for i in range(len(self.__lista[num])):
                    
                    if self.__lista[num][i]==None:
                        print("{0:^10d} {1:^10d} {2:^10d} {3:^10d}".format(i,0,0,0))
                    else:
                        print("{0:^10d} {1:^10d} {2:^10d} {3:^10d}".format(i,self.__lista[num][i].getTemperatura(),self.__lista[num][i].getHumedad(),self.__lista[num][i].getPresion()))
        else:
            print("Numero no valido")
    def promTemperatura(self):
        print("{0:^10} {1:^10}".format("Hora",'PromedioTemperatura'))
        for i in range(24):
            acum=0
            con=0
            for j in range(len(self.__lista)):
                    if len(self.__lista[j])!=0:
                        if self.__lista[j][i]!=None:
                            con+=1
                            acum+=self.__lista[j][i].getTemperatura()
            if(con!=0 ):
                print("{0:^10d}{1:^24.2f}".format(i,acum/con))
            else:
                print("{0:^10d}{1:^24d}".format(i,0))
    def mayorMenor(self):
        mayorTemperatura=0
        menorTemperatura=99
        mayorHumedad=0
        menorHumedad=99
        mayorPresion=0
        menorPresion=999
        diamayorTemp=0
        diamenorTemp=0
        diamayorHum=0
        diamenorHum=0
        diamayorPresion=0
        diamenorPresion=0
        horamayorTemp=0
        horamenorTemp=0
        horamayorHum=0
        horamenorHum=0
        horamayorPresion=0
        horamenorPresion=0
        for i in range(len(self.__lista)):
            for j in range(24):
                if len(self.__lista[i])!=0:
                    if(self.__lista[i][j]!=None):
                        if (self.__lista[i][j].getTemperatura()>mayorTemperatura):
                            mayorTemperatura=self.__lista[i][j].getTemperatura()
                            diamayorTemp=i+1
                            horamayorTemp=j
                        if (self.__lista[i][j].getTemperatura()<menorTemperatura):
                            menorTemperatura=self.__lista[i][j].getTemperatura()
                            diamenorTemp=i+1
                            horamenorTemp=j
                        if(self.__lista[i][j].getHumedad()>mayorHumedad):
                            mayorHumedad=self.__lista[i][j].getHumedad()
                            diamayorHum=i+1
                            horamayorHum=j
                        if(self.__lista[i][j].getHumedad()<menorHumedad):
                            menorHumedad=self.__lista[i][j].getHumedad()
                            diamenorHum=i+1
                            horamenorHum=j
                        if(self.__lista[i][j].getPresion()>mayorPresion):
                            mayorPresion=self.__lista[i][j].getPresion()
                            diamayorPresion=i+1
                            horamayorPresion=j
                        if(self.__lista[i][j].getPresion()<menorPresion):
                            menorPresion=self.__lista[i][j].getPresion()
                            diamenorPresion=i+1
                            horamenorPresion=j
        print("dia:{} y hora:{} de mayor temperatura".format(diamayorTemp,horamayorTemp))
        print("dia:{} y hora:{} de menor temperatura".format(diamenorTemp,horamenorTemp))
        print("dia:{} y hora :{} de mayor humedad ".format(diamayorHum,horamayorHum))
        print("dia:{} y hora :{} de menor humedad ".format(diamenorHum,horamenorHum))
        print("dia:{} y hora:{} de mayor presion".format(diamayorPresion,horamayorPresion))
        print("dia:{} y hora{} de menor presion".format(diamenorPresion,horamenorPresion))
    def funcionTestManejador(self):
        print("Funcion test Manejador:")
        manejador1=ManejadorRegistro()
        print("Metodo agregarDias")
        manejador1.agregarDias(30)
        print("Metodo agregarHoras")
        manejador1.agregarHoras(24)
        print("Metodo cargar registro")
        manejador1.cargarRegistro(Registro(20,30,700),1,15)
        manejador1.cargarRegistro(Registro(24,40,800),10,23)
        print("Metodo cargarArchivo")
        manejador1.cargarArchivo()
        print("Metodo buscarDia:")
        manejador1.buscarDia(6)
        manejador1.buscarDia(20)
        print("Metodo promTemperatura:")
        manejador1.promTemperatura()
        print("Metodo mayorMenor")
        manejador1.mayorMenor()