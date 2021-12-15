from annealing import QuickAnnealing
from best_sample import sample
import math

NameFun = ["Химмельблау 1 с начальной точкой (0;0) ", "Химмельблау 2 с начальной точкой (0;0)",
           "Вуда с начальной точкой (-3; -1; -3; -1)", "Вуда с начальной точкой (2; -1; -3; -1)",
           'Пауэлла с начальной точкой (1; 1; 1; 1)', "Пауэлла с начальной точкой (3; -1; 0; 1)"]

def f1(x):
    return 4 * pow((x[0] - 5), 2) + pow((x[1] - 6), 2)


def f2(x):
    return pow(x[0] * x[0] + x[1] - 11, 2) + pow(x[0] + x[1] * x[1] - 7, 2)


def f3(x):
    return (100 * (x[1] - x[0] ** 2) ** 2 +
            (1 - x[0]) ** 2 +
            90 * (x[3] - x[2] ** 2) ** 2 +
            (1 - x[2]) ** 2 +
            10.1 * ((x[1] - 1) ** 2 + (x[3] - 1) ** 2) +
            19.8 * (x[1] - 1) * (x[3] - 1))


def f4(x):
    x1, x2, x3, x4 = x
    return ((x1 + 10 * x2) ** 2 +
            5 * (x3 - x4) ** 2 +
            (x2 - 2 * x3) ** 4 +
            10 * (x1 - x4) ** 4)


def f5(x):
    x, y = x
    A = x * math.cos(1.571) - y * math.sin(1.571)
    B = x * math.sin(1.571) + y * math.cos(1.571)
    return (0.1 * 1.5 * A) ** 2 + (0.1 * 0.8 * B) ** 2 - 4 * math.cos(0.8 * 1.5 * A) - 4 * math.cos(0.8 * 0.8 * B) + 8


def f6(x):
    x, y = x
    return (-10 / (0.005 * (x ** 2 + y ** 2) - math.cos(x) * math.cos(y / math.sqrt(2)) + 2)) + 10

def f7(x): 
    x, y = x
    return (1.5 - x + x*y) ** 2 + (2.25 - x + x*(y**2)) ** 2 + (2.625 - x + x*(y**3)) ** 2

def f8(x): 
    x, y = x
    return 100 * math.sqrt(abs(y - 0.01*(x**2))) + 0.01 * abs(x + 10)


funcsToTest = [f1, f2, f3, f3, f4, f4]
startPoint = [[0., 0.], [1., 1.], [-3., -1., -3., -1.], [2., -1., -3., -1.], [1., 1., 1., 1.], [3., -1., 0., 1.]]
for i in range(6):
    print(f"\nТест функции {NameFun[i]}")
    for j in range(5):
        res = sample(startPoint[i], 1, funcsToTest[i])
        print(f"Точка минимума: {res[0]}")
        print(f"Минимум: {funcsToTest[i](res[0]):.{10}f}")
        print(f"Количество итераций: {res[1]}")
    print('_______________________________________')

print('\nТест функции «Растригина овражная с поворотом осей» с начальной точкой (5;5)')
for j in range(5):
    res = QuickAnnealing([-5., 5.], 0.05, f5)
    print(f"Точка минимума: {res}")
    print(f"Минимум: {f5(res):.{10}f}")
print('______________________________________')

print('\nТест функции «Griewank» с начальной точкой (1;1)')
for j in range(5):
    res = QuickAnnealing([-2., 2.], 0.005, f6, N=10000)
    print(f"Точка минимума: {res}")
    print(f"Минимум: {f6(res):.{10}f}")

print('\nТест функции Била с начальной точкой (3;0.5)')
for j in range(5):
    res = QuickAnnealing([3., 0.5], 0.05, f7)
    print(f"Точка минимума: {res}")
    print(f"Минимум: {f7(res):.{10}f}")

print('\nТест функции Букина N 6 с начальной точкой (-10;1)')
for j in range(5):
    res = QuickAnnealing([-10., 1.], 0.05, f8)
    print(f"Точка минимума: {res}")
    print(f"Минимум: {f8(res):.{10}f}")