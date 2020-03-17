# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:51:38 2020

@author: genin
"""

import unittest
from TP08 import process_user_input, puiss2, puiss3, puiss4

    
class MyTestCase(unittest.TestCase):
    def test_puiss2(self):
        self.assertEqual(puiss2([4, 9]), [16, 81])
    
    def test_puiss3(self):
        self.assertEqual(puiss3([1, 2, 3]), [1, 8, 27])
        
    def test_puiss4(self):
        self.assertEqual(puiss4([1, 2, 3]), [1, 16, 81])
    
    def test_functions(self):
        function_name =  'sum'
        valeurs = [1, 2]
        self.assertEqual(process_user_input(valeurs, function_name), 3)
        #or
        self.assertEqual(process_user_input([1, 2], 'sum'), 3)
        self.assertEqual(process_user_input([1, 2], 'max'), 2)
        self.assertEqual(process_user_input([1, 2], 'min'), 1)
        self.assertEqual(process_user_input([1, 2], 'avg'), 1.5)
        self.assertEqual(process_user_input([1, 1], 'sd'), 0)
        self.assertEqual(process_user_input([1, 2, 3], 'median'), 2)
                  
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    import unittest
    unittest.main()

  