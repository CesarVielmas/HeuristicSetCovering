#Importing librarys
from cmath import isnan
from ctypes import sizeof
from multiprocessing.dummy import Array
import string

from numpy import array
import numpy as np
#Start Reading
f = open("reader1.txt","r");
filas = f.read(4);
columnas = f.read(5);
#filas and columnas (rows and columns)
filas = int(filas.replace(" ",""));
columnas = int(columnas.replace(" ",""));
#Ready Reading data
contador = 0;
sets =[];
costos = [];
#cuantity of sets start
for i in range(columnas):
   valorSet = [];
   for i in range(filas):
      valorSet.append(0);
   sets.append(valorSet);
#cuantity of sets finish
contador = 0;
inicio = 0;
elements = 0;
stopFirstCoverElement = 0;
counterForAnyElement = 0;
counterElementPosition = -1;
print("Cantidad de filas: ",filas);
print("Cantidad de columnas: ",columnas);
#sets values start
for numero1 in f.readlines():
   #Cost of any set
   if(inicio == 0):
    for elementos in np.array_split(numero1.split(" "),40):
      if(contador == columnas):
         inicio+=1;
         continue;
      if(elementos!="" and elementos!= " " and elementos!= "\n" and int(elementos)>0):
         costos.append(int(elementos));
         contador+=1;
   
   #Asignement values in binary for every set
   elif(inicio>0):
      #take how many sets cover any element
      for elementos in np.array_split(numero1.split(" "),40):
         if(elementos!="" and elementos!= " " and elementos!= "\n" and int(elementos)>0 and stopFirstCoverElement<1):
            elements = int(elementos);
            stopFirstCoverElement+=1;
            counterElementPosition +=1;
         #when take the element how many sets cover , give the value 1 if the element encounter in the cover
         elif(elements!=0 and counterForAnyElement<elements):
            if(elementos!="" and elementos!= " " and elementos!= "\n" and int(elementos)>0):
              #element x its cover for ...
              sets[int(elementos)-1][counterElementPosition] = 1;
              counterForAnyElement+=1;
         
         elif(counterForAnyElement == elements):
              counterForAnyElement = 0;
              stopFirstCoverElement = 0;
              elements = 0;
#sets values finish
print("Cantidad de costos: ",len(costos));
print("Cantidad de sets: ",len(sets));
#algorithm
contador = 0;
contador2= 0;
contador3 = 0;
improvement = [];
exitCicle = True;
valueMax = 0;
costAcumulate = 0;
print("Resultado:");
while(exitCicle):
   #values of improvement for any set start
   for valorSet in sets:
      for i in valorSet:    
         if(i == 1):
            contador+=1;
      improvement.append(contador);
      contador = 0;
   contador = 0;
#values of improvement for any set finish

   #position of best improvement
   for improvements in improvement:
      if(improvements == max(improvement)):
         print("-Set: ",contador+1);
         costAcumulate += costos[contador];
         valueMax +=max(improvement);
         break;
      contador+=1;
   #delete the position in all sets for the next improvement
   for i in range(columnas):
      for valueSet in sets:
         if(contador2 == contador):
            for i in valueSet:
               if(i == 1):
                  for k in range(columnas):
                     sets[k][contador3] = 0;
               
               contador3+=1;
         contador2+=1;
   
   #Reset values
   improvement = [];
   contador2 = 0;
   contador3 = 0;
   contador  = 0;
   #when complete all cover elements then exit 
   if(valueMax>=filas):
      print("Costo: ",costAcumulate);
      exitCicle = False;

   
   
   




    
          
