import numpy as np
from scipy.optimize import minimize
from typing import Callable
from functions import Functions

def GZ(func: Callable[..., float], size: int, optim: Callable[[Callable[[float], float], float, float], float], e, ListH):
    k = 0
    x = [[0]*size]
    h = np.array(ListH)
    z = 0.1
    iterations = 0
    while proverkaEN(h) > z:
        iterations += 1
        x.append([0]*size)
        for i in range(size):
            args = x[k].copy()
            def optim_func(x):
                nonlocal i, func, args
                args[i] = x
                return func(*args)
            a = optim(optim_func, args[i], h[i])
            x[k + 1][i] = a
        if any([abs(x[k + 1][i] - x[k][i]) > e for i in range(size)]):
            k += 1
            continue
        h *= z
    return x[k+1], iterations



def proverkaEN(h: np.array):
    return np.sqrt((h**2).sum())


def optim(function, x0, h):
    res = minimize(function, x0, method='nelder-mead', options={'xatol': h, 'disp': False})
    return res.x[0]


def valuefunction1(*args):
    return Functions.func1(args)


def valuefunction2(*args):
    return Functions.func2(args)

def valuefunction3(*args):
    return Functions.func3(args)

def valuefunction4(*args):
    return Functions.func4(args)

def GaussaZeydel_print(*args):
    number_fun = int(input("Введите номер уравнение: "))
    h = []
    if number_fun == 1 or number_fun == 2:
        quantity = 2
        h = [1., 1.]
    else:
        quantity = 4
        h = [1., 1., 1., 1.]
    x0 = []
    for i in range(quantity):
        x0.append(float(input('Введите x(' + str(i + 1) + '): ')))
    e = float(input("Введите погрешность: "))
    if number_fun == 1:
        func = valuefunction1
    elif number_fun == 2:
        func = valuefunction2
    elif number_fun == 3:
        func = valuefunction3
    elif number_fun == 4:
        func = valuefunction4
    [result, iterations] = GZ(func, quantity, optim, e, h)
    for i in range(quantity):
        result[i] = round(result[i], 5)
    print('x* = ', result)
    print('Кол-во итераций: ', iterations)