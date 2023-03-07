#Author: Cesar Vielmas
from cmath import isnan
from ctypes import sizeof
from multiprocessing.dummy import Array
import string

from numpy import array
import numpy as np
#inicio Reader
f = open("reader1.txt","r");
filas = f.read(4);
columnas = f.read(4);
#filas y columnas
filas = int(filas.replace(" ",""));
columnas = int(columnas.replace(" ",""));
print("Columnas:",columnas,"\nFilas:",filas);
contador = 0;
sets =[];
costos = [];
#numeros de los sets
while(contador<columnas):
   sets.append(contador+1);
   contador+=1;
contador = 0;
contadorSet = 0;

setsIteraciones = 0;
contadorValores = 0;
valoresSets = [];
posibleNumero = 0;
setsCompletos = [];
inicio = 0;
for numero1 in f.readlines():
   #Costo Cada Set principio
   if(inicio == 0):
    for elementos in np.array_split(numero1.split(" "),40):
      if(contador == columnas):
         continue;
      if(elementos!="" and elementos!= " " and elementos!= "\n" and elementos=="1"):
         costos.append(elementos);
         contador+=1;
   #Recubrimiento de cada set
   for elementos in np.array_split(numero1.split(" "),40):
      #Dando con el resultado de cuantos sets Recubre
      if(elementos!="" and elementos!= " " and elementos!= "\n"):
         if(elementos!= "1" and contadorSet==0):
            setsIteraciones = int(elementos);
            contadorSet+=1;
      #Si ya se dio con el valor de cuantas veces debe iterar , entonces
      if(setsIteraciones!=0):
         while(contadorValores<columnas+1):
            valoresSets.append(0);
            contadorValores+=1;

         if(elementos == ""):
            posibleNumero = 1;

         elif(posibleNumero == 1 and elementos!="" and elementos!=" " and elementos!="\n"):
            posibleNumero = 2;

         elif(posibleNumero == 2 and elementos=="\n"):
            posibleNumero = 3;
         elif(posibleNumero == 2 and elementos!= "\n"):
            posibleNumero = 0;

         if(elementos!="" and elementos!= " " and elementos != "\n"):
            if(posibleNumero != 3):
               valoresSets[int(elementos)] = 1;
              

         if(posibleNumero == 3):
            setsCompletos.append(valoresSets);
            valoresSets = [];
            contadorSet = 0;
            setsIteraciones = 0;
            inicio = 1;
            contadorValores = 0;
            posibleNumero = 0;
        
print(len(costos));
print(len(setsCompletos));
contador = 0;
#Verlo en tabla
for sets in setsCompletos:
   print("Set ",contador+1,": ",sets);
   contador +=1;
#Fin Reader
terminar = True;
valorCompleto = 0;
valoresMejoras = [];
#Algoritmo
while(terminar):
#Mejoras Valores
 for sets in setsCompletos:
    for valores in sets:
       if(valores == 1):
          valorCompleto+=1;
    valoresMejoras.append(valorCompleto);
    valorCompleto = 0;
#Posicion de las mejoras
 

