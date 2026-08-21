import numpy as np
import math 
import matplotlib.pyplot as plt 

# valor verdadeiro
u = 2.71828182846

# critério de parada 
na = 6 
Eppara = 0.5 * 10**(2-na)

print("Critério de Parada:", Eppara)

def serieMaclarium(x,n):
    return (x**n) / math.factorial(n)

# definição de x
x = 1 

# inicialização da variável que vai somar os valores
soma = 0 

# inicialização das listas que vão guardar os dados para os gráficos
I = []
SOMA = []
EPT = []

# Número de termos 
n = 6
for i in range(0,n): # vou variar para toda essa faixa 

    soma += serieMaclarium(x,i)
    Ept = abs((u - soma)/u) * 100
    
    print(f"Iteração {i} | Ept %: {Ept} | Soma: {soma}")

    # Correção dos comandos '.append()' para adicionar nas listas certas
    I.append(i)
    SOMA.append(soma)
    EPT.append(Ept)

# ------------- gráficos -------------
# Criando um gráfico do Erro (EPT) por número de iterações (I)
plt.plot(I, SOMA, '-or', label="Estimativa")
plt.legend()
plt.grid()
plt.title("Decaimento do Erro na Série de Maclaurin")
plt.xlabel("Número da Iteração (i)")
plt.ylabel("Estimativa $(e^1=e)$")
plt.show()


plt.plot(I, EPT, '-ob', color='blue', label="$E_{pt} \ (\%)$")
plt.legend()
plt.title(" Erro ")
plt.xlabel("Número da Iteração (i)")
plt.ylabel("$E_{pt} \ (\%)$")
plt.grid()
plt.show()

# Imprimindo a lista de interações no final, como você pediu
print("Lista de iterações (I):", I)



