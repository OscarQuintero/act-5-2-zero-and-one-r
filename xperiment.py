# -*- coding: utf_8 -*-

import csv
import random

#Variables 

ConjuntoInicial = []
ConjuntoEntrenamiento = []
ConjuntoPrueba = []

#Declaración de Funciones


'''Lee el archivo CSV en la ruta especificada 
	y devuelve una lista de diccionarios que es el conjunto de datos'''
def extraerConjuntoInicialDe(rutaDelArchivo):
	conjunto = []
	with open(rutaDelArchivo) as ArchivoOrigen:
		reader = csv.DictReader(ArchivoOrigen)
			
		for row in reader:
			conjunto.append(row)

		return conjunto

'''Toma un conjunto de datos inicial y de manera aleatoria
	separa en dos conjuntos de datos disjuntos, uno para entrenamiento y otro para pruebas
	Se requiere 
	el conjunto de datos inicial que no sufrirá cambios
	el conjunto de datos en el que se guardarán las instancias de entrenamiento
	el conjunto de datos donde se guardarán las instancias de prueba
	El porcentaje de instancias que se utilizarán de entrenamiento.'''
def separarConjuntoInicialEnEntrenamientoYPrueba(conjuntoI, conjuntoE, conjuntoP, PorcentajeEntrenamiento):
	conjuntoE[:] = []
	conjuntoP[:] = conjuntoI[:]
	numTuplasEntrenamiento = len(conjuntoI)*PorcentajeEntrenamiento/100
	#print("Tuplas para entrenamiento: ", numTuplasEntrenamiento)
	i = 0
	while i < numTuplasEntrenamiento:
		#print i 
		instanciaAleatoriaPos = random.randint(0, len(conjuntoP)-1)
		conjuntoE.append(conjuntoP[instanciaAleatoriaPos])
		conjuntoP.pop(instanciaAleatoriaPos)
		#print('Tamaño C Entrenamiento:', len(conjuntoE),' Tamaño C Prueba:', len(conjuntoP))

		i+=1
	#print conjuntoE
	
	return

'''conjunto es el data set a analizar, y el nombre del atributo clase es nombreClase 
	para la busqueda en los disccionarios
	Se devuelve una lista con los valores posibles de las clases (dominioClase)'''
def obtenerDominioDeClase(conjunto, nombreClase):
	dominioClase = []
	pass
	return dominioClase

def obtenerFrecuenciaDeClase(conjunto, nombreClase, dominioClase):

	return

#Flujo pricnipal del programa
print('----------------------------------------')
print("Lectura del archivo CSV... ")
print('----------------------------------------')

ConjuntoInicial = extraerConjuntoInicialDe('db.csv')

print('--------------------------------')
print("Conjunto de Datos Inicial:")
print('----------------------------------------')
# print ConjuntoEntrenamiento
# print ConjuntoPrueba
print ConjuntoInicial

print('----------------------------------------')
print("Separando en dos conjuntos disjuntos....")
print('----------------------------------------')
separarConjuntoInicialEnEntrenamientoYPrueba(ConjuntoInicial, ConjuntoEntrenamiento, ConjuntoPrueba, 70)
#print ConjuntoInicial

print('----------------------------------------')
print("Conjunto de Datos de Entrenamiento:")
print('----------------------------------------')
print ConjuntoEntrenamiento
print('----------------------------------------')
print("Conjunto de Datos de Prueba:")
print('----------------------------------------')
print ConjuntoPrueba

#Determinar el dominio de clase
#Determinar clase con más frecuencia
#Determinar 
#


# print ConjuntoInicial[3]
#print ConjuntoInicial

print('--------------------------------')
print("....")
print('--------------------------------')