from origenydestino import validarorigenydestino
from paquetes import paquetesListado, printpaquete
from precio import choose

#consultar origen y destino
origenDestino=validarorigenydestino()
#Arreglo apra guardar el origen y destino ingresados por el cliente
destino=origenDestino[1]
#Buscar paquetes disponibles al usuario de acuerdo al destino ingresado
paquetes=paquetesListado(destino)

#Imprimir los paquetes correspondientes
printpaquete(paquetes)

#seleccionar y Calcular precio
choose(paquetes)

