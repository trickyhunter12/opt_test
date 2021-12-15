import random
import math
import numpy as np

# алгоритм имитации отжига

def QuickAnnealing(x0, t0, f, N=2500):
    k = 1
    random.seed(45)
    dim = len(x0)
    x = np.array(x0)
    t = t0
    while k < N:
        #xtemp = x + np.random.standard_cauchy(dim)
        xtemp = x + np.random.standard_normal(dim)
        if f(xtemp) < f(x):
            x = xtemp
        else:
            p = math.exp((f(x)-f(xtemp))/t)
            if random.random() < p:
                x = xtemp
        k += 1
        #t = t0/(pow(k, 1/dim))
        t = t0 / math.log(1 + k)
    return x
