import numpy as np
from scipy import optimize
from typing import Callable, List
from functions import Functions


def Gesse(x, e, funct):
    N = x.shape[0]
    gess = np.zeros((N, N))
    gd = optimize.approx_fprime(x, funct, e ** 2)
    eps = np.linalg.norm(gd) * np.finfo(np.float32).eps
    for i in range(N):
        x0 = 1. * x[i]
        x[i] = x0 + eps
        gd1 = optimize.approx_fprime(x, funct, e ** 2)
        gess[:, i] = ((gd1 - gd) / eps).reshape(x.shape[0])
        x[i] = x0
    return gess


def NR(x0: List[float], e, funct: Callable[..., float]):
    currentx = np.array(x0)
    k = 0
    gradient = optimize.approx_fprime(currentx, funct, e ** 2)
    while np.linalg.norm(gradient) ** 2 > e:
        gessM = Gesse(currentx, e, funct)
        invGesseM = np.linalg.inv(gessM)
        p = -1 * invGesseM * gradient
        diag = p.diagonal()
        scP = np.ravel(diag)
        a = optimize.minimize_scalar(lambda x: funct(currentx + scP * x), bounds=(0,)).x
        currentx += a * scP
        k += 1
        gradient = optimize.approx_fprime(currentx, funct, e ** 2)
    return currentx, k


def valuefunction(number, *args):
    if number == 1:
        return Functions.func1
    elif number == 2:
        return Functions.func2
    elif number == 3:
        return Functions.func3
    elif number == 4:
        return Functions.func4


def NewtonRafson_print(*args):
    number_fun = int(input("Введите номер уравнение: "))
    if number_fun == 1 or number_fun == 2:
        quantity = 2
    else:
        quantity = 4
    x0 = []
    for i in range(quantity):
        x0.append(float(input("Введите х(%d): " % (i + 1))))
    e = float(input("Введите погрешность: "))
    result, count = NR(x0, e, valuefunction(number_fun))
    for i in range(quantity):
        result[i] = round(result[i], 5)
    print('х* = ', result)
    print('Число итераций = ', count)
