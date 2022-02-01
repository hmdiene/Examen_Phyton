import numpy as np

def factorielle(n):
    p=1
    for i in range(1,int(n)+1):
        p=p*i
    return p

print(factorielle(5))