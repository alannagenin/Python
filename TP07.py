# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:36:02 2020

@author: genin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:37:15 2020

@author: genin
"""
import numpy as np
#import time


registre_valeurs = {}
registre_fonction = {'sum': sum} #Ajouter la fonction sum au registre

# Question 3 : implementez remplissez le registe avec les fonctions 'max', 'min', 'moyenne' et 'ecart-type'
registre_fonction['max'] = max
registre_fonction['min'] =  min
registre_fonction['moyenne'] = np.mean
registre_fonction['ecart-type'] = np.std
registre_fonction['mediane'] = np.median

# ------------------------------------------------ Fonctions puissance -------------------------------------------------------
#dans ipython
#def modn(n):
#    def monmodulo(p):
#        return p % n
#    return monmodulo
#
#modn(2)(10)
    
def puiss1(x):
    return x
registre_fonction['puiss1'] = puiss1

def puiss2(liste):
    return [x**2 for x in liste]
registre_fonction['puiss2'] = puiss2

def puiss3(liste):
    return [x**3 for x in liste]
registre_fonction['puiss3'] = puiss3

def puiss4(liste):
    return [x**4 for x in liste]
registre_fonction['puiss4'] = puiss4

#somme de x a la puissance n
#def puiss(x, n):
#    s = 0
#    for i in range(x):
#        s += x **n 
#    return s

def puiss(n):
    def pown(liste):
        return [x**n for x in liste] #or pow(x, n) 
    return pown

puiss(4)(2)
registre_fonction['puiss'] = puiss

#fonction puissance n-ieme
#def pow_n_1(f, n):
#    return f**n
#registre_fonction['pow_n_1'] = pow_n_1

##list at the power n
#def pown(liste, n):
#    return [x**n for x in liste]
#registre_fonction['pown'] = pown

# ------------------------------------------------------------ Loop -----------------------------------------------------------

def loop():
    #valeurs
    dataset_name = input("Entrez le nom du dataset : ")
    if dataset_name not in registre_valeurs:
        valeurs = input("Entrez les valeurs séparées par une virgule : ")
        registre_valeurs[dataset_name] = valeurs = [float(valeur) for valeur in valeurs.split(",")]#permet d'affecter dans "valeurs" egalement
    
    #fonction
    fonction_name = input("Donnez le nom de la fonction a utiliser : ")#Afficher le résultat
    if fonction_name in registre_fonction:
        if fonction_name[1:5] == 'puiss'.lower():
            n = fonction_name[5:6]
            res = registre_fonction[fonction_name](registre_valeurs[dataset_name]) 
        else :
            res = registre_fonction[fonction_name](registre_valeurs[dataset_name])
        print("Le résultat de la fonction", fonction_name, "est : ", res)
    
    #debugeur
#    import pdb
#    pdb.set_trace()

if __name__ == "__main__":
  while True:
      message = input("Faites entrée pour continuer et quittez en tapant 'exit' puis entrée ")
      if message == "exit".lower():
          break
      loop()




# ----------------------------------------------------- Registering functions --------------------------------------------------

def fonction():
  pass

registre_fonction[fonction.__name__] = fonction

#registering functions
def register_function(name, function):
    registre_fonction[name] = function

#registering my function in the register
def f(x):
    return x+2
register_function("my_fonction", f)
    
#registering functions using *args **kwargs and @
#@register_function


