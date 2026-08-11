import numpy as np
import math as sp 
import matplotlib.pyplot as plt 

#valor verdadeiro
u = 2.71828182846

# critério de parada 
n = 6 
Eppara = 0.5*10**(2-n)

print(Eppara)

def serieMaclarium(x,n):
    return (x**n)/math.factorial(n)

