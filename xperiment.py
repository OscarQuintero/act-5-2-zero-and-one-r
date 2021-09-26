# -*- coding: utf_8 -*-

print('--------------------------------')
print("Lectura del archivo CSV ")
print('--------------------------------')

import csv

ConjuntoInicial = []
ConjuntoEntrenamiento = []
ConjuntoPrueba = []

def extraerConjuntoInicialDe(ruta):
	print ("En construcción")
	with open(ruta) as ArchivoOrigen:
		reader = csv.DictReader(ArchivoOrigen)
			
		for row in reader:
			ConjuntoInicial.append(row)



    


extraerConjuntoInicialDe('db.csv')



print ConjuntoInicial[3]
print ConjuntoInicial

print('--------------------------------')
print("Proceso....")
print('--------------------------------')