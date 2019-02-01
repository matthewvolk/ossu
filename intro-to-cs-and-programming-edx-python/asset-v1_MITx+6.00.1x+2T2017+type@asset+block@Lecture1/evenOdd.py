# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:03:23 2016

@author: ericgrimson
"""
cont = 1

while cont:
    x = int(input('Enter an integer: '))
    if x%2 == 0:
        print('')
        print('Even')
    else:
        print('')
        print('Odd')
    print('Done with conditional')
    cont = int(input('Go again? (1 = yes, 0 = no): '))