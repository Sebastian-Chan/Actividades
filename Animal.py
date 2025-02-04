#SEBASTIAN ALBERTO CHAN HERNANDEZ
#INGENIERIA EN TI Y NEGOCIOS DIGITALES
#00550218
#EJERCICIO CLASES Y OBJETOS

import random
class Animal:

#CONSTRUCTOR
    def __init__(self,nombre,tipo,peso,edad):
        self.__nombre=nombre
        self.__tipo=tipo
        self.__peso=peso
        self.__edad=edad
#------------------------------------------------

    def generarEdad(self):
        edad=random.randint(1,6)
        return edad
    
    def generarPeso(self):
        peso=random.randint(3,30)
        return peso
    
    
    #DEFINICION DE GETTERS Y SETTERS
    def setEdad(self,edad):
        self.__edad=self.generarEdad()

    def getEdad(self):
        return self.__edad

    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setTipo(self,tipo):
        self.__tipo=tipo

    def getTipo(self):
        return self.__tipo
    
    def setPeso(self,peso):
        self.__peso=self.generarPeso()

    def getPeso(self):
        return self.__peso
    
    #------------------------------------------------------
    
    #DEFINICION DE ACCION
    def decirDatos(self):
        print(f"Hola soy un: {self.getNombre()} de tipo: {self.getTipo()}, tengo: {self.getEdad()} años y peso: {self.getPeso()} kg")
    
#CODIGO
def main():
    listaMamiferos=["Jirafa", "Cuyo","Leon","Elefante","Perro","Gato","Caballo","Oso pardo"]
    listaAves= ["Aguila", "Halcon", "Buho", "Loro", "Pinguino", "Flamenco", "Pavo real", "Ganso"]
    listaReptiles=["Cocodrilo", "Lagarto", "Iguana", "Cobra", "Gecko", "Vibora", "Anaconda", "Caiman"]


    for i in range (5):
        #GENERAR UN VALOR RANDOM DEL 1 AL 3 PARA SELECCIONAR EL TIPO DE ANIMAL
        eleccion_animal=random.randint(1,3)
        
        if (eleccion_animal==1):
            nombre=random.choice(listaMamiferos)
            listaMamiferos.remove(nombre)
            tipo="Mamifero"

        elif (eleccion_animal==2):
            nombre=random.choice(listaAves)
            listaAves.remove(nombre)
            tipo="Ave"

        else:
            nombre=random.choice(listaReptiles)
            listaReptiles.remove(nombre)
            tipo="Reptil"

#CREACION DEL OBJETO
        animal = Animal(nombre, tipo, None, None)

        peso = animal.generarPeso()
        edad = animal.generarEdad()
        animal.setEdad(edad)
        animal.setPeso(peso)

        animal.decirDatos()

if __name__=="__main__":
    main()