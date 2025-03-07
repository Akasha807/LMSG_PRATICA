#Localiza el arhivo
import Llista

#Le declara los valores
noms = ["Joan","Li","Akasha"]
nom = "Li"

#Busca en el archivo que busque noms, nom que devuelva algo
pos = Llista.esta_nom(noms, nom)

#Hacé la condiciónes
if(pos == True):
    print(nom, "es troba a la llista")
else:
    print(nom, "NO es troba a la llista")


