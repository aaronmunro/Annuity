import pandas as pd
import numpy as np

def probability(t):
    return (0.6 - 0.01 * t) / 0.6

def discount(i, t):
    return (1 + i) ** -t

def probabilities(n):
    return [probability(year) for year in range(n)]

def discounts(i, n):
    return [discount(i, year) for year in range(n)]

def EPV(i, n, CF):
    return CF * np.dot(probabilities(n), discounts(i, n))

if __name__ == "__main__":
    i = int(input("Input i: "))
    n = int(input("Input n: "))
    CF = int(input("Input CF: "))
    print("EPV: ", EPV(i, n, CF))
