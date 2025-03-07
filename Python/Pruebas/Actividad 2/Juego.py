#Buscamos el arhivo
import Diccionario

#Hacemos un bucle de true que obigue al usuaria poner algo si o si
#Hasta que no salga del programa

while(true)
#Imprimimos la opciones
print("1. Mostrar diccionar")
print("2. Afegir entrades")
print("3. Mostrar entrada")
print("4. Esborrar entrada")
print("5. Modificar entrada")
print("\n0. Sortir\n\n\n")

#Leemos lo que pone el usuario
read = input()

#Hacemos condiciónes
print("Introduce la clave")
clave = input()

print("Introduce el valor")
valor = input()

Diccionario.miDiccionari[clave]=valor

#Diccionario.miDiccionari.pop("genere")
del Diccionario.miDiccionari["genere"]


print(Diccionario.miDiccionari)
#Mostrem tot el dicionari
#for i in Diccionario:
# print(Diccionario[i])





