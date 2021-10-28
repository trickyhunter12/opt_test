machineAccurate = 0.000000001

from functions import Functions
import numpy as np
from scipy import optimize

Path = []

#class FlatcherRivseFunc:
def FletcherRivse(x0, h, eps, f):
    currentX = np.array(x0)
    Path.append(currentX)
    h = np.array(h)
    n = len(x0)
    k = 0

    gradient = optimize.approx_fprime(currentX, f, eps * eps)
    previousGradient = 1
    pk = -1 * gradient

    while np.linalg.norm(gradient) ** 2 + machineAccurate > eps:
        if k == 0 or (k + 1) % n == 0:
            previous_pk = pk
            pk = -1 * gradient
            beta_k = 1
        else:
            beta_k = (np.linalg.norm(gradient) ** 2) / (np.linalg.norm(previousGradient) ** 2)
        previous_pk = pk
        pk = -1 * gradient + beta_k * previous_pk
        ak = optimize.minimize_scalar(lambda x: f(currentX + pk * x), bounds=(0,)).x
        currentX = currentX + ak * pk
        Path.append(currentX)
        k += 1
        previousGradient = gradient
        gradient = optimize.approx_fprime(currentX, f, eps * eps)
    return currentX, k


def value_function(number, *args):
    if number == 1:
        return Functions.func1
    elif number == 2:
        return Functions.func2
    elif number == 3:
        return Functions.func3
    elif number == 4:
        return Functions.func4


def FlatcherRivse_print(*args):
    number = int(input("Введите номер уравнения: "))
    if number == 1 or number == 2:
        quantity = 2
    else:
        quantity = 4
    x0 = []
    h = []

    for i in range(quantity):
        x0.append(float(input('Введите x(%d): ' % (i + 1))))
        h.append(1)

    e = float(input('Введите погрешность: '))
    result, count = FletcherRivse(x0, h, e, value_function(number))

    for i in range(quantity):
        result[i] = round(result[i], 5)
    print('x* = ', result)
    print('Число итераций = ', count)
