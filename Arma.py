class Arma:
    def __init__(self,nombre, tipo, daño, durabilidad, elemento):
        self.nombre = nombre
        self.tipo = tipo
        self.daño = daño
        self.durabilidad = durabilidad
        self.elemento = elemento
        pass

    #Metodos
    
    def Aumentar_daño(self):
        nuevo_daño = input("\nIngresa el nuevo daño: ")
        self.daño = nuevo_daño
        return print("\nDaño Actualizado\n")

    def Cambiar_elemento(self):
        nuevo_elemento = input("\nNuevo Elemento: \n")
        self.elemento = nuevo_elemento
        return print("\nElemento cambiado\n")

    def Actualizar_durabilidad(self):
        
        durabilidad_perdida = int(input("Durabilidad perdida: "))
        self.durabilidad -= durabilidad_perdida

        if self.durabilidad <= 0:
            self.durabilidad = "Arma Rota"
        else:
            pass    
        return print("\nEstado del arma alterado!\n")

    def Mostrar_datos(self):
        print(f"\n--- [{self.nombre}] ----\n")
        print("Tipo: ", self.tipo)
        print("Daño: ", self.daño)
        print("Durabilidad: ", self.durabilidad)
        print("Elemento: ", self.elemento)
        print("_____________________________\n")

#Objetos

Arco = Arma("Arco Elfo Oscuro","Distancia",20,45,"Hielo")
Espada = Arma("Mata Dragones","Cuerpo a Cuerpo",100,150,"N/A")


#Mostrar
Arco.Mostrar_datos()
Espada.Mostrar_datos()

#Actualizar
Arco.Actualizar_durabilidad()

#Mostrar
Arco.Mostrar_datos()
Espada.Mostrar_datos()