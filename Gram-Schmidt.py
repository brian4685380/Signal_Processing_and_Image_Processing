import numpy as np

def f1(x) :
    return 1
def f2(x) :
    return x
def f3(x) :
    return x ** 2
def f4(x) :
    return x ** 3
def f5(x) :
    return x ** 4

def phi1(x) :
    sum = 0
    for i in range (0, 11) :
        sum += f1(i) * f1(i)
    return f1(x) / (sum ** 0.5)
def g2(x) :
    sum = 0
    for i in range (0, 11) :
        sum += f2(i) * phi1(i)
    return f2(x) - sum * phi1(i)
def phi2(x) :
    sum = 0
    for i in range (0, 11) :
        sum += g2(i) * g2(i)
    return g2(x) / (sum ** 0.5)
def g3(x) :
    sum = 0
    sum2 = 0
    for i in range (0, 11) :
        sum += f3(i) * phi1(i)
    for i in range (0, 11) :
        sum2 += f3(i) * phi2(i)
    return f3(x) - sum * phi1(x) - sum2 * phi2(x)
def phi3(x) :
    sum = 0
    for i in range (0, 11) :
        sum += g3(i) * g3(i)
    return g3(x) / (sum ** 0.5)
def g4(x) :
    sum = 0
    sum2 = 0
    sum3 = 0
    for i in range (0, 11) :
        sum += f4(i) * phi1(i)
    for i in range (0, 11) :
        sum2 += f4(i) * phi2(i)
    for i in range (0, 11) :
        sum3 += f4(i) * phi3(i)
    return f4(x) - sum * phi1(x) - sum2 * phi2(x) - sum3 * phi3(x)
def phi4(x) :
    sum = 0
    for i in range (0, 11) :
        sum += g4(i) * g4(i)
    return g4(x) / (sum ** 0.5)
def g5(x) :
    sum = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for i in range (0, 11) :
        sum += f5(i) * phi1(i)
    for i in range (0, 11) :
        sum2 += f5(i) * phi2(i)
    for i in range (0, 11) :
        sum3 += f5(i) * phi3(i)
    for i in range (0, 11) :
        sum4 += f5(i) * phi4(i)
    return f5(x) - sum * phi1(x) - sum2 * phi2(x) - sum3 * phi3(x) - sum4 * phi4(x)
def phi5(x) :
    sum = 0
    for i in range (0, 11) :
        sum += g5(i) * g5(i)
    return g5(x) / (sum ** 0.5)