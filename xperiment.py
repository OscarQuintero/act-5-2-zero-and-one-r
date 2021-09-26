# -*- coding: utf_8 -*-

import csv
import random

#Variables 

ConjuntoInicial = []
ConjuntoEntrenamiento = []
ConjuntoPrueba = []

#Declaración de Funciones

def extraerConjuntoInicialDe(rutaDelArchivo):
	Conjunto = []
	with open(rutaDelArchivo) as ArchivoOrigen:
		reader = csv.DictReader(ArchivoOrigen)
			
		for row in reader:
			Conjunto.append(row)

		return Conjunto

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



# print ConjuntoInicial[3]
#print ConjuntoInicial

print('--------------------------------')
print("....")
print('--------------------------------')