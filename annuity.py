import pandas as pd
import numpy as np

def q4_tP40(t):
    return((0.6-0.01*t)/(0.6))

def q4_discount(i, t):
    return((1+i) ** (-t))

def q4_epv(CF, i, n):
    EPV = 0
    for t in list(range(0,n)):
        EPV += (q4_discount(i, t) * q4_tP40(t))
    return(CF * EPV)

# print(q4_epv(i = 0.04, n = 10))



# print(q4_discount(0.08, 9)*q4_tP40(9))

# print(q4_discount(0.08, 10)*q4_tP40(10))

#print(list(range(0,10)))

def inter(t):
    return(q4_discount(0.08, t)*q4_tP40(t))

print(q4_epv(CF = 5000,i = 0.08, n = 10))

# Linear Algebra methods

# Vector of probs.

def Prob(n):
    probs = []
    for year in range(0, n):
        probs.append((0.6-0.01 * year)/(0.6))
    return(probs)

# Vector of discount factors.

def discount(i, n):
    discounts = []
    for year in range(0, n):
        discounts.append((1+i) ** (-year))
    return(discounts)

def EPV(i, n, CF):
    print(CF * np.dot(Prob(n), discount(i, n)))

EPV(0.08, 10, 5000)