#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:26:17 2020

@author: alanna
"""

import numpy as np

registre_valeurs = {'a': [6, 7, 8, 9]}
registre_fonction = {'sum': sum,
                     'max': max,
                     'min': min,
                     'avg': np.mean,
                     'sd': np.std,
                     'median': np.median}




# ---------------------------------------------------------- Fonctions puissance --------------------------------------------------------------------------
    
def puiss1(x):
    return x
registre_fonction['puiss1'] = puiss1

#correction
#liste = [1, 2, 6]
#for element in liste:
#    print(element)

def puiss2(liste):
    return [x**2 for x in liste]
registre_fonction['puiss2'] = puiss2

def puiss3(liste):
    return [x**3 for x in liste]
registre_fonction['puiss3'] = puiss3

def puiss4(liste):
    return [x**4 for x in liste]
registre_fonction['puiss4'] = puiss4

def puiss(n):
    def pown(liste):
        return [x**n for x in liste] #or pow(x, n) 
    return pown

#-------------------------------------------------------------------------- Input and calculating ---------------------------------------------

def process_user_input(valeurs, function_name):
    #calculating the value of the function
    if function_name in registre_fonction:
        res = registre_fonction[function_name](valeurs)
    return res


def loop():
    #values
    dataset_name = input("Dataset name : ")
    if dataset_name not in registre_valeurs:
        valeurs = input("Entrez les valeurs séparées par une virgule : ")
        registre_valeurs[dataset_name] = valeurs = [float(valeur) for valeur in valeurs.split(",")]#permet d'affecter dans "valeurs" egalement
    valeurs = registre_valeurs[dataset_name]

    #name of the function
    function_name = input("Donnez le nom de la fonction a utiliser : ")
    
    #call the function process_user_input
    res = process_user_input(valeurs, function_name)
    print("Le résultat de la fonction", function_name, "est : ", round(res, 2))
      
    

#Ecrivez des tests pour les questions de la séance précédente. Vous pouvez commencer avec assert.
#exemple :
liste1 = [1,2,3]
liste2 = [1, 2 , 4-1]
assert liste1 == liste2

#tests (ne pas utiliser tel quel)
#self.assertListEqual(liste1, liste2)
#self.assertEqual(liste1, liste2, f"liste1 {liste1} ne vaut pas {liste2}")


#https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual Pour verifier que deux listes sont égales.
#à toute fin utile : https://github.com/cgte/cours_iut/blob/master/demo_test.py ne recopiez pas tout le fichier.


#------------------------------------------------------------------------- Loop ------------------------------------------------------------------------------

if __name__ == "__main__":
  while True:
      message = input("Faites entrée pour continuer et quittez en tapant 'exit' puis entrée ")
      if message == "exit".lower():
          break
      loop()








