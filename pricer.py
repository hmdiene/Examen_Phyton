from subprocess import call
import numpy as np
import scipy.stats as si
import sympy as sy
import sympy.stats as systats

def euro_vanilla_call(S, K, T, r, sigma):    
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

print(euro_vanilla_call(50, 100, 1, 0.05, 0.25))