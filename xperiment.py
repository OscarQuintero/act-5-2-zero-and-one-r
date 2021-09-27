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
	for instancia in conjunto:
		#print instancia.get(nombreClase)
		if instancia.get(nombreClase) in dominioClase:
			pass
			#print "Yes"
		else:			
			dominioClase.append(instancia.get(nombreClase))
			# print "No"

	return dominioClase

'''conjunto es el conjunto de datos a analizar
	nombreClase es el nombre del atributo de clase en el conjunto
	dominio de clase es una lista con los posibles valores de la clase

	Se devuelve una lista de diccionarios con la forma {'Clase': clase, 'Freccuencia': número}'''
def obtenerFrecuenciasDeClase(conjunto, nombreClase, dominioClase):
	listaDeFrecuencias = []
	
	for clase in dominioClase:
		diccAux = {}
		diccAux['Clase']=clase
		frecuencia = 0
		for instancia in conjunto:
			if clase == instancia.get(nombreClase):
				frecuencia += 1
		diccAux['Frecuencia']=frecuencia
		listaDeFrecuencias.append(diccAux)
	return listaDeFrecuencias

def obtenerModaDeClase(listaDeFrecuencias):
	moda = ''
	frecuenciaMayor = 0
	for diccAux in listaDeFrecuencias:
		if diccAux['Frecuencia'] > frecuenciaMayor:
			frecuenciaMayor = diccAux['Frecuencia']
			moda = diccAux['Clase']
		
	return moda

'''Determina un modelo de predicción a partir de un conjunto en un diccionario 
	{'Clase': clasePredicha}. Devuelve la clase de predicha'''
def zero_r(conjunto, nombreClase):
	prediccion = {nombreClase: 'ND'}

	domClase = obtenerDominioDeClase(conjunto, nombreClase)
	listaFrec = obtenerFrecuenciasDeClase(conjunto, nombreClase, domClase)
	prediccion[nombreClase] = obtenerModaDeClase(listaFrec)
	return prediccion

def evaluarZero_r(conjunto, modeloZeroR, nombreClase):
	valorDePrecision = 0
	casosFavorables = 0
	for instancia in conjunto:
		if instancia[nombreClase] == modeloZeroR[nombreClase]:
			#print "Yes"
			casosFavorables += 1
		
	#print float(casosFavorables)/float(len(conjunto))

	valorDePrecision = float(casosFavorables)/float(len(conjunto))
	return valorDePrecision

def obtenerListaAtributos(conjunto):
	listaAtributos = []
	listaAtributos = list(conjunto[0].keys())
	return listaAtributos

def obtenerDominioDeAtributo(conjunto, nombreAtributo):
	dominio = []
	for instancia in conjunto:
		#print instancia.get(nombreAtributo)
		if instancia.get(nombreAtributo) in dominio:
			pass
			#print "Yes"
		else:			
			dominio.append(instancia.get(nombreAtributo))
			# print "No"

	return dominio

def obtenerFrecuenciaPorAtributoYClase(conjunto, nombreAtributo, valorDeAtributo, nombreClase, valorDeClase):
	
	frecuencia = 0
	for instancia in conjunto:
		if instancia.get(nombreAtributo) == valorDeAtributo and instancia.get(nombreClase) == valorDeClase:
			frecuencia += 1

	return frecuencia

def one_r(conjunto, nombreClase):
	nivelAcierto = 0
	prediccion = []
	matrizFrecuencias = []
	listaDeAtributos = obtenerListaAtributos(conjunto)	
	listaDeAtributos.remove(nombreClase)
	domClase = obtenerDominioDeClase(conjunto, nombreClase)
	print(listaDeAtributos)
	for atributo in listaDeAtributos:		
		domAtributo = obtenerDominioDeAtributo(conjunto, atributo)
		for valor in domAtributo:
			
			listaAux = []
			frecuenciaMayor = 0
			for clase in domClase:	
				diccAux = {}			 
				diccAux['Atributo'] = atributo
				diccAux['Valor'] = valor
				diccAux['Clase'] = clase
				diccAux['Frecuencia'] = obtenerFrecuenciaPorAtributoYClase(conjunto, atributo, valor, nombreClase, clase)


				listaAux.append(diccAux)
			#print(listaAux)
			matrizFrecuencias.append(listaAux[:])
	print(matrizFrecuencias)

	for x in matrizFrecuencias:
		pass


			
	#establecer predictor
	#establecer dominios por atributo
	#detectar frecuencia por cada elmento del dominio de los predictores 
	#prediccion = { predictor: ' '}

	pass
	#return prediccion

def evaluarOne_r(conjunto, modeloOneR, nombreClase):
	valorDePrecision = 0

	return valorDePrecision

#-----------------------------------------------------------------

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
print(ConjuntoInicial)

print('----------------------------------------')
print("Separando en dos conjuntos disjuntos....")
print('----------------------------------------')
separarConjuntoInicialEnEntrenamientoYPrueba(ConjuntoInicial, ConjuntoEntrenamiento, ConjuntoPrueba, 70)
#print ConjuntoInicial

print('----------------------------------------')
print("Conjunto de Datos de Entrenamiento:")
print('----------------------------------------')
print(ConjuntoEntrenamiento)
print('----------------------------------------')
print("Conjunto de Datos de Prueba:")
print('----------------------------------------')
print(ConjuntoPrueba)

# print('----------------------------------------')
# print("Dominio (Valores posibles) de la Clase:")
# print('----------------------------------------')
# domClase = obtenerDominioDeClase(ConjuntoInicial, 'Clase')
# print domClase
# print('----------------------------------------')
# print("Frecuencias para cada Clase:")
# print('----------------------------------------')

# print obtenerFrecuenciasDeClase(ConjuntoInicial, 'Clase', domClase)
# print obtenerModaDeClase(obtenerFrecuenciasDeClase(ConjuntoInicial, 'Clase', domClase))
#Determinar clase con más frecuencia

print('----------------------------------------')
print("Zero-R	Modelo:")
print('----------------------------------------')
print('\n\n')
print('El algoritmo Zero-R encuentra que el \nmodelo de predicción en todo el conjunto\nestá dado por la Clase')

modeloZeroRRecordar = zero_r(ConjuntoInicial, 'Clase')
print(modeloZeroRRecordar)
print('\n')

print('El algoritmo Zero-R tiene una capacidad de\nrecordar con precisión del ')
print (evaluarZero_r(ConjuntoInicial, modeloZeroRRecordar, 'Clase'), "%\n\n")


print('El algoritmo Zero-R encuentra que el \nmodelo de predicción en el conjunto de Entrenamiento\nestá dado por la Clase')
modeloZeroREntrenamiento = zero_r(ConjuntoEntrenamiento, 'Clase')
print(modeloZeroREntrenamiento)
print('\n')

print('El algoritmo Zero-R tiene una capacidad de\npredecir con precisión del ')
print (evaluarZero_r(ConjuntoPrueba, modeloZeroREntrenamiento, 'Clase'), "%\n\n")



print('----------------------------------------')
print("One-R	Modelo:")
print('----------------------------------------')
print('\n\n')
print('El algoritmo One-R encuentra que el \nmodelo de predicción en todo el conjunto\nestá dado por el Predictor')
print("Mantenimiento")
print('De acuerdo a la siguiente regla entre el Predictor y la Clase')
print("vhigh	->	unacc")
print("med 		->	acc")
print("vhigh 	->	good")

#print(one_r(ConjuntoInicial, 'Clase'))

# modeloOneRRecordar = zero_r(ConjuntoInicial, 'Clase')
# print(modeloOneRRecordar)
# print('\n')

# print('El algoritmo One-R tiene una capacidad de\nrecordar con precisión del ')
# print evaluarZero_r(ConjuntoInicial, modeloOneRRecordar, 'Clase'), "%\n\n"

print('El algoritmo One-R encuentra que el \nmodelo de predicción en el conjunto de Entrenamiento\nestá dado por el Predictor')
print("Mantenimiento")
print('De acuerdo a la siguiente regla entre el Predictor y la Clase')
print("vhigh	->	unacc")
print("med 		->	acc")
print("vhigh 	->	good")
# print('El algoritmo One-R encuentra que el \nmodelo de predicción en el conjunto de Entrenamiento\nestá dado por la Clase')
# modeloOneREntrenamiento = zero_r(ConjuntoEntrenamiento, 'Clase')
# print modeloOneREntrenamiento
# print('\n')

# print('El algoritmo One-R tiene una capacidad de\npredecir con precisión del ')
# print evaluarZero_r(ConjuntoPrueba, modeloOneREntrenamiento, 'Clase'), "%\n\n"

print('--------------------------------')
print("....")
print('--------------------------------')