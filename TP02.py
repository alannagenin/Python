# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:51:27 2020

@author: genin
"""
import time

#Question 1: créer une fonction qui renvoie une dictionnaire avec les les clefs 'kind', 'duration' et 'weight' et 'identifier'
def create_gift(kind):
    print(f"\nCreating {kind} gift")
    time.sleep(1)
    if kind == "small":
        weight = 0.5
        duration = 1
        return {"kind": kind, "duration": duration, "weight": weight}
    elif kind == "medium":
        weight = 2
        duration = 2
        return {"kind": kind, "duration": duration, "weight": weight}

    elif kind == "large":
        weight = 5
        duration = 3
        return {"kind": kind, "duration": duration, "weight": weight}

    else:
        print(f"Error {kind} is unknown")


#def create_gifts(kinds):
#    for kind in kinds:
#        t = time.time()
#        yield create_gift(kind)
#        print(f"Time taken for creating gift {time.time() - t:.4f}")
#    # return [ for kind in kinds]


def create_gifts(kinds):
    return [create_gift(kind) for kind in kinds]

sledge = {"gifts": [], "max_load": 12, "time_per_gift": 0.5}

def wrap_gift(gift):
    print("Starting to wrap")
    time.sleep(gift["duration"])
    print("Wrapped a %s gift" % gift["kind"])


def compute_free_load(sledge):
    return sledge["max_load"] - sum(gift["weight"] for gift in sledge["gifts"])


def sledge_load(sledge):
    return sum(gift["weight"] for gift in sledge["gifts"])


def take_gift(sledge, gift):
    if gift["weight"] <= compute_free_load(sledge):
        sledge["gifts"].append(gift)
        return 1
    else:
        return 0


# Tiens mais il faudrait qu'on puisse savoir si le cadeau a été pris
# Soit a la valeur de return
# (exception)


def ship(sledge):
    print(f"Shipping {len(sledge['gifts'])} gifts")
    print(f"{sledge_load(sledge)} kg to be shipped")

    for gift in sledge["gifts"]:
        time.sleep(sledge["time_per_gift"])
    print(f"Shipped  {len(sledge['gifts'])}")
    sledge["gifts"] = []


def process_gifts(gifts):
    for gift in gifts:
        wrap_gift(gift)
        taken = take_gift(sledge, gift)
        if taken == 1:
            print(f"Current load {sledge_load(sledge)}")
            continue #passer à l'element suivant ds une boucle (continuer un traitement dans une boucle)
        else:
            ship(sledge)
            taken = take_gift(sledge, gift)
            if taken == 0:
                print("Error, sledge should take the gift after shipping")
    else:
        ship(sledge)


def create_and_process(gift_types):
    process_gifts(create_gifts(gift_types))


#if __name__ == "__main__":
#    import sys
#
#    if len(sys.argv) == 2:
#        n_gifts = int(sys.argv[1])
#    else:
#        n_gifts = 15
#    from random import choices
#
#    gift_types = choices(["small", "medium", "large"], k=n_gifts)
#    create_and_process(gift_types)









#Question 6.a : créez les classes Gift et Sledge, implémentez les methodes __init__ pour les deux classes et la methode wrap pour gift    

class gift:
    def __init__(self, kind):#pas de return dans un __init__
        #print(self)
        print(f"\nCreating {kind} gift")
        time.sleep(1)
        if kind == "small":
            self.weight = 0.5
            self.duration = 1
        elif kind == "medium":
            self.weight = 2
            self.duration = 2   
        elif kind == "large":
            self.weight = 5
            self.duration = 3
        else:
            print(f"Error {kind} is unknown")
        self.kind = kind
    
    
    def wrap(self):
        print("Starting to wrap")
        time.sleep(self.duration)
        print("Wrapped a %s gift" % self.kind)
    
    def create_gift(self, kinds):
        [self.kind for kind in self.kinds]
            
cadeau = gift('small')
cadeau.duration#accès à la durée d'emballage
cadeau.wrap()#appel à la méthode

l = ['small', 'medium', 'small']
l.create_gift()

class sledge:
    def __init__(self):
        self.gifts = []
        self.max_load = 12
        self.time_per_gift = 0.5
    
    
#Question 7: Utilisez une méthode de classe pour fournir une interface plus simple pour creer des cadeaux.
        
        
#Question 8: Utilisez des variables de classe pour les caracteristiques du traineau là ou cela vous semble judicieux.
