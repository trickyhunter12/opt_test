import random
import numpy as np
from scipy import optimize


# алгоритм наилучшей пробы
def sample(x0, t0, f, b=0.001, M=12, N=10, R=1.0e-5):
    random.seed(42)
    dim = len(x0)
    x = np.array(x0)
    t = t0
    # step1
    k = 0
    j = 1
    while True:
        # step2
        ksi = 2*np.random.rand(dim)-np.ones(dim)
        # step3
        y = x+t*(ksi/np.linalg.norm(ksi))
        #step4
        ym = optimize.minimize(f, y).x
        #step4(a)
        if f(ym) < f(x):
            x = ym
            k += 1
            if k < N:
                j = 1
                continue
            else:
                return x, k
       
        else:
            if t <= R:
                return x, k
            else:
                t *= b
                j = 1
                continue

