import math
import numpy as np
from sympy import *
from scipy.misc import derivative
import sys

print('Выберите метод: ')
print('1 : Метод Пауэлла ')
print('2 : Метод Фибоначчи ')
print('3 : Метод средней точки')

method = int(input())
while method < 1 or method > 3:
    print('Неверный номер метода')
    method = int(input())

print('Выберите одну из функций: ')
print('1 : (x-1)^2 ')
print('2 : 4x^3 - 8x^2 - 11x + 5 ')
print('3 : x + 3/x^2 ')
print('4 : (x + 2.5) / (4 - x^2) ')
print('5 : -sin(x) - sin(3x)/3 ')
print('6 : -2sin(x) - sin2x - 2/3sin3x')

function = int(input())
while function < 1 or function > 6:
     print('Неверный номер функции')
     function = int(input())


def f(x: float):
        if function == 1:
            try:
                return (x - 1) ** 2
            except:
                print("Oops!  That was no valid number.  Try again...")
                sys.exit(1)

        if function == 2:
            try:
                return 4 * x ** 3 - 8 * x ** 2 - 11 * x + 5
            except:
                print("Oops!  That was no valid number.  Try again...")
                sys.exit(1)

        if function == 3:
            try:
                return x + 3 / x ** 2
            except:
                print("Oops!  That was no valid number.  Try again...")
                sys.exit(1)

        if function == 4:
            try:
                return (x + 2.5) / (4 - x ** 2)
            except:
                print("Oops!  That was no valid number.  Try again...")
                sys.exit(1)

        if function == 5:
            try:
                return (-1) * math.sin(x) - math.sin(3 * x) / 3
            except:
                print("Oops!  That was no valid number.  Try again...")
                sys.exit(1)

        if function == 6:
            try:
                return (-2) * math.sin(x) - math.sin(2 * x) - (2 / 3) * math.sin(3 * x)
            except:
                print("Oops!  That was no valid number.  Try again...")
                sys.exit(1)

e = 0.01
d = e/10
N = 11



# ---------------------------  метод Дэвиса-Свенна-Кэмпи 1.1  -------------------------------------------------


def search_local_min():
    x0 = float(input('Введите x0: '))
    h = float(input('Введите h: '))
    f0 = f(x0)
    a = b = x0
    if f0 > f(x0 + h):
        a = x0
    elif f(x0 - h) >= f0:
        a = x0 - h
        b = x0 + h
        return a, b
    else:
        b = x0
        h = -h

    def xk(k: int):
        return x0 + (2 ** (k - 1)) * h

    def assign_if(is_a, value):
        nonlocal a, b
        if is_a:
            a = value
        else:
            b = value

    k = 2
    while True:
        xk0, xk1 = xk(k), xk(k - 1)
        if f(xk0) >= f(xk1):
            assign_if(h < 0, xk0)
            break
        else:
            assign_if(h > 0, xk1)
        k += 1

    return a, b


# ---------------------------  Pawell-search 1.2.5 -------------------------------------------------
# Метод параболической аппроксимации Пауэлла
def powell(func, a: float, b: float, eps=0.01):
    # step 1
    x1 = a
    x2 = (a + b) / 2
    x3 = b
    X = [x1, x2, x3]
    iterations = 0
    # step 2
    while (True):
        iterations += 1
        min_x = X[0]
        for i in X:
            if  func(i) < func(min_x):
                min_x = i

        # step 3
        num = (X[1] ** 2 - X[2] ** 2) * func(X[0]) + (X[2] ** 2 - X[0] ** 2) * func(X[1]) + (
                    X[0] ** 2 - X[1] ** 2) * func(X[2])
        denum = (X[1] - X[2]) * func(X[0]) + (X[2] - X[0]) * func(X[1]) + (X[0] - X[1]) * func(X[2])
        X.append(0.5 * (num / denum))
        # step 4
        if (abs(X[3] - min_x) <= eps):
            break
        # step 5
        X.sort()
        # step 6
        max_x = 0
        for i in range(4):
            if (func(X[i]) > func(X[max_x])):
                max_x = i
        X.pop(max_x)
        if (iterations > 1000):
            print("Метод не сходится. Превышено максимальное кол-во итераций")
            sys.exit(1)


    # step 7
    return X[-1], iterations


# ---------------------------  Fibonacci 1.2.3 -------------------------------------------------

# Метод Фибоначчи
class FibonacciImpl:
    arr = [0,1,1]

    def calculate(self, num: int):
        if num < len(self.arr):
            return self.arr[num]
        else:
            for i in range(len(self.arr)-1, num):
                new_fib = self.arr[i-1] + self.arr[i]
                self.arr.append(new_fib)
            return self.arr[num]

fib_impl = FibonacciImpl()

def fib(num):
    global fib_impl
    return fib_impl.calculate(num)

def metod_fib(func, a, b, eps=0.001, sigma=0.001 / 10):
    N = int((b - a) / (2 * eps))
    print('iterations - ',N)
    x1 = a + fib(N - 2) / fib(N) * (b - a)
    x2 = a + fib(N - 1) / fib(N) * (b - a)
    for k in range(2, N - 2):
        if func(x1) <= func(x2):
            b = x2
            x2 = x1
            x1 = a + fib(N - k - 3) / fib(N - k - 1) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + fib(N - k - 2) / fib(N - k - 1) * (b - a)
    x2 = x1 + sigma
    if func(x1) <= func(x2):
        b = x2
    else:
        a = x1
    return (a + b) / 2, N

# --------------------------- Method-Avg-Point -------------------------------------------------

def average_point(a,b,eps=0.001, sigma=0.001 / 10):
    iterations = 0
    while (b-a)/2 >= eps:
        iterations += 1
        x1 = 1/2*(a+b) - sigma
        x2 = 1/2*(a+b) + sigma
        fx1 = f(x1)
        fx2 = f(x2)
        if (iterations > 1000):
            print("Метод не сходится. Превышено максимальное кол-во итераций")
            sys.exit(1)
        if fx1 <= fx2:
            b = x2
        else:
            a = x1
        if (b-a)/2 < eps:
            xPoint = (a+b)/2
            return xPoint, iterations


def main():
    if method == 1:
        [res, i] = powell(f, a, b)
        print('Ответ: ', res, 'Кол-во итераций', i)
    if method == 2:
        [res, i] = metod_fib(f, a, b)
        print('Ответ: ', res, 'Кол-во итераций', i)
    if method == 3:
        [res, i] = average_point(a, b)
        print('Ответ: ', res, 'Кол-во итераций', i)

[a, b] = search_local_min()
print(a,",",b)

if __name__ == "__main__":
     main()