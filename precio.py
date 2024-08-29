
def choose (paquetes):
     choose=int(input("Ingrese el numero correspondiente al paquete que desea: "))
     number=int(input("Digite la cantidad de personas que adquiriran el paquete: "))
     paquete=paquetes[choose-1]
     if  choose == 1:
        valor= paquete[6]
        #Eliminar los puntos 
        valorc=valor.replace(".","")
        precio=int(valorc)*number
        #volver a agregar los puntos
        precioc="{:,}".format(precio).replace(",", ".")

        print("el precio a pagar es de: $", precioc)
     return precioc      

