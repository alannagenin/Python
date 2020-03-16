# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
>>> gift = create_gift('small')
>>> gift['duration']
0.5
"""

import unittest
from module_gift import create_gift, take_gift
from module_sledge import ship

#dans la log : 
#print(demo_test.__doc__)
#assert True == True
#assert True == False

def unefonction5():
    ''' une fonction qui renvoie toujours 5 
    >>> unefonction5()
    5
    '''
    return 5

def exemple_doctest(*args, **kwargs):
    """
    >>> exemple_doctest(1,2,3, a=2)
    ((1, 2, 3), {'a': 2})
    
    exemple_doctest(1,7)
    ((1, 7), {})
    """    
    return args, kwargs

def process_gift(gift, sledge):
    # do something with gift and sledge
    pass

class MyTestCase(unittest.TestCase):
    def test_take_gift(self):
        petit, moyen, grand1, grand2, grand3 = [
                create_gift(kind) for kind in 
                ['small', 'medium', 'large', 'large', 'large']]
        sledge = {'gifts': [], 'max_load': 12}
        self.assertEqual(take_gift(sledge, petit), True)
        self.assertTrue(take_gift(sledge, moyen))
        self.assertTrue(take_gift(sledge, grand1))
        self.assertFalse(take_gift(sledge, grand2), f"We should not accept this gift due to lack of free load")
    
    def test_ship(self):
        petit, moyen, grand1, grand2, grand3 = [
                create_gift(kind) for kind in 
                ['small', 'medium', 'large', 'large', 'large']]
        sledge = {'gifts': [], 'max_load': 12}
        self.assertEqual(take_gift(sledge, petit), True)
        self.assertTrue(take_gift(sledge, moyen))
        self.assertTrue(take_gift(sledge, grand1))
        self.assertFalse(take_gift(sledge, grand2), f"We should not accept this gift due to lack of free load")
    
        ship(sledge)
        self.assertEqual(sledge['gifts'], [])#vérifier que la liste est bien vide après ship()
        self.assertEqual(len(sledge['gifts']), 0)            
    
    
class ShowSetUpTestCase(unittest.TestCase):
    def setUp(self):
        self.gifts = [create_gift(kind) for kind in 
                ['small', 'medium', 'large', 'large', 'large']]#creation liste de cadeaux
        self.sledge = {'gifts': [], 'max_load': 12}
        
    def test_ship(self):
        """ On vérifie que si on ne peut plus prendre de cadeau on les envoie en livraison
        """
        gifts, sledge = self.gifts, self.sledge #recree sinon on garde les infos contenues dans le module sledge
        batch1 = gifts[:3]
        for gift in batch1:
            process_gift(gift, sledge)
        restants = gifts[3:]
        process_gift(restants[0], sledge)
        self.assertEquals(sledge['gifts'], [restants[0]])
      
    def test_deuxieme_fonctionalite(self):#que doit faire cette fonction ?
        gifts, sledge = self.gifts, self.sledge
        # à vous de jouer
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    import unittest
    unittest.main()