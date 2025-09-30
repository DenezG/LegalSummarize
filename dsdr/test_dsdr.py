#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from dsdr import DSDR

class TestDSDR(unittest.TestCase):
    
    def test_lin(self):
        '''
        >>> DSDR.lin(V, m=2, lamb=0.1)
        [2, 4]
        '''
        V = [[1,2,4,0],
             [0,1,0,0],
             [1,1,0,0],
             [0,0,1,0],
             [0,0,1,1]]
        L = DSDR.lin(V, m=2, lamb=0.1)
        print(L)
        # show summary
        for i in L:
            print(V[i])

    def test_non(self):
        '''
        >>> DSDR.non(V, gamma=0.1)
        [ 0.49301097  0.49301097  0.6996585   0.49301097  0.70211699]
        '''
        V = [[1,0,0,0],
             [0,1,0,0],
             [1,1,0,0],
             [0,0,1,0],
             [0,0,1,1]]
        beta = DSDR.non(V, gamma=0.1)
        print(beta)
        # show summary
        for score, v in sorted(zip(beta, V), reverse=True):
            print(score, v)

if __name__ == '__main__':
    unittest.main()