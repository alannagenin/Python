# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:39:25 2020

@author: genin
"""
#une liste
maliste = [1,1,2,3,5,4,7]
maliste[::-1]
maliste[::-2]

#difference entre entier et flottant
flottant = 6
entier = 6.0
[x.real for x in [entier, flottant]]

chaine = "Bonjour"
dir(chaine)#methodes disponibles pour cette variable

chaine.__add__(" Alanna")
chaine

iut = "IUT"
iut.__add__(" Paris")
#ou
iut + " Paris"

""""dans le cadre des cadeaux, on aimerait ajouter deux dictionnaires (ex traineau += cadeau) mais cela n'est pas possible
--> pb si deux clefs sont identiques"""

def afficher(*args):#quand on ne sait pas trop combien on a de paramètres
    for i in args:
        print(i)

afficher(1)
afficher(1, 2)
afficher(1, 2, 3, 4, 5, 6)

a, b = 1, 2
a, *b, c = 1, 2, 3, 4  #assignation multiple

from collections import namedtuple #permet de nommer des tuples
Point_NT = namedtuple('Point2D', 'x y')
p = Point_NT(1 ,3)
p.x, p.y
p

class Point2D: #jusque là c'est la même chose que le name tuple
    ''' Définit un point en 2D avec x et y comme attributs'''
    def __init__(self, x, y):
        self.x = x
        self.y = y # Un exemple d'affectation

notre_point = Point2D(1,3) #mais ce n'est pas pareil
notre_point.x, notre_point.y
notre_point
print(notre_point)



class Point2D:
    ''' Définit un point en 2D avec x et y comme coordonnées '''
    def __init__(self, x, y): #ne pas faire def __init__(self, x=None, y=None): car on aura rien dans x et y 
        self.x, self.y = x, y # Un exemple d'affectation

    def __str__(self):
        return f"Point2D:{{'x': {self.x}, 'y': {self.y}}}"

    def norm(self):
        return (self.x**2 + self.y**2) ** (0.5)
    
    def translation(self, x, y):
        self.x += x
        self.y += y
        
notre_point = Point2D(3,4)
notre_point.norm()
notre_point.translation(1,2) #ne renvoie rien
print(notre_point)


class A :
    pass

a = A() 
a.b = 12
a.__dict__
a.c = 36
a.__dict__

# avec @property on n'est plus obligé de mettre des parentheses










class Conteneur:
    pass


gg = Conteneur()

# On peut ensuite ajouter des données dans les objets renvoyés par
# l'appel à Conteneur()


gg.entier = 1
print(gg.entier)

gg.liste = [1, 2, 3, 4]
gg.autreliste = [None, "bonjour"]

gg.a = "a1"

# On souhaite creer dans notre conteneur


def make_point(conteneur, x, y):
    setattr(conteneur, "x", x)
    conteneur.y = y
    return conteneur


gg = make_point(gg, 1, 2)
print(gg)
print(gg.x)
print(gg.y)


def make_point_2(conteneur, x, y):
    conteneur.x = x
    conteneur.y = y


point = Conteneur()
make_point_2(point, 3, 4)
point.x


Conteneur.__init__ = make_point_2
nouveau_point = Conteneur(5, 6)
nouveau_point.x


def stringify_point(point):
    return f"({point.x},{point.y})"


print(stringify_point(nouveau_point))
Conteneur.__str__ = stringify_point
print(nouveau_point)

# Ce qui est équivalent à

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


point1 = Point(5, 6)
print(point1)

from pprint import pprint
mat = [[1, 2,][3, 4]]
pprint(mat)


#Nombres binaires
bin(9)
bin(9)[2:]
bin(9)[2:].split('1')
[len(item) for item in bin(9)[2:].split('1')]
[len(item) for item in bin(529)[2:].split('1') if item]
max([len(item) for item in bin(529)[2:].split('1') if item])
max([len(item) for item in bin(20)[2:].split('1') if item])
max([len(item) for item in bin(20)[2:].split('0').split('1') if item])
max([len(item) for item in bin(15)[2:].split('0').split('1') if item])
max([len(item) for item in bin(15)[2:].split('0').split('1')])
max([len(item) for item in bin(20)[2:].split('0')])