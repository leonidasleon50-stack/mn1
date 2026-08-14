import numpy as np
import math as sp 
import matplotlib.pyplot as plt 

#valor verdadeiro
u = 2.71828182846

# critério de parada 
na = 6 
Eppara = 0.5*10**(2-na)

print(Eppara)

def serieMaclarium(x,n):
    return (x**n)/math.factorial(n)

#definição de x
x = 1 

#inicialização de variáveis

soma  = 0 
#Número de termos 
n = 6
for i in range(0,n-1): #vou varia para toda essa faixa 

    soma += serieMaclarium(x,i)
    pritn("A soma e:",soma)



