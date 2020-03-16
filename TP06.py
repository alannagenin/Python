# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:37:15 2020

@author: genin
"""
import numpy as np
import time

def f():
    return 3

print(f)
print(f())

class Exc:
    def __init__(self, a):
        self.a = a
    def faire(self):
        print("Hello world")
        return self.a ** 3

a = Exc(3)
a.faire
print(a)
print(a.faire)
print(a.faire())

#registre de fonction
registre = {'f' : f}#permet de stocker des fonctions

def lk():
    return 468334.5837

registre['lk'] = lk
print(registre) #{'f': <function f at 0x00000251F0DCBEA0>, 'lk': <function lk at 0x00000251F0DCBF28>}
print(registre['lk'])#<function lk at 0x00000251F0DCBF28>
print(registre['lk']())#appel dynamique de fonction

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                           Debut du TP
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
registre_valeurs = {}
registre_fonction = {'sum':sum} #Ajouter la fonction sum au registre

# Question 3 : implementez remplissez le registe avec les fonctions 'max', 'min', 'moyenne' et 'ecart-type'
registre_fonction['max'] = max
registre_fonction['min'] =  min
registre_fonction['moyenne'] = np.mean
registre_fonction['ecart-type'] = np.std
registre_fonction['median'] = np.median


# ------------------------------------------------ Fonctions puissance -------------------------------------------------------

def puiss1(x):
    x**1

def puiss2(x):
    x**2

def puiss3(x):
    x**3

def puiss4(x):
    x**4

def puiss(n, x):
    s = 0
    for i in range(x):
        s += x **n 
    return s

def loop():
    #valeurs
    dataset_name = input("Entrez le nom du dataset : ")
    if dataset_name not in registre_valeurs:
        valeurs = input("Entrez les valeurs séparées par une virgule : ")
        registre_valeurs[dataset_name] = [float(valeur) for valeur in valeurs.split(",")]
    
    #fonction
    fonction_name = input("Donnez le nom de la fonction a utiliser : ")#Afficher le résultat
    if fonction_name in registre_fonction:
        res = registre_fonction[fonction_name](registre_valeurs[dataset_name])
        print("Résultat : ", res)

if __name__ == "__main__":
  while True:
      message = input("Faites entrée pour continuer et quittez en tapant 'exit' puis entrée ")
      if message == "exit".lower():
          break
      loop()

def chrono(fonction):
    def chronometre():
        t1 = time()
        fonction() #appel à la fonction
        t2 = time()
        print("%2f" % t2 - t1)
        return
    return chronometre

fonction_chrono = chrono(puiss)

#chronometrer une fonction a n-arguments
def chorno(fonction):
    def chronometree(*args):
      t = time()
      res = fonction(*args)
      print("%2f" % time - t)
      return
  return chronometree

#fonction puissance n-ieme

def pow_n_1(f, n):
    return f**n
