import numpy as np
import matplotlib.pyplot as plt
import math
# https://math.stackexchange.com/questions/778297/how-to-arrange-functions-in-increasing-order-of-growth-rate-providing-fn-og
def c(n):
    f = 2 * math.log(n) + math.log(math.log(n))
    return f

def b(n):
    g = math.pow(n,2)+1
    return g

def a(n):
    return math.pow(2,n)+1

def d(n):
    return math.log(n)

def e(n):
    return math.log(n)+math.pow(2,n)
#
# def k(n):
#     return -np.sqrt(n)

n = np.array(np.linspace(2, 5, 500))
functions = [a,b,c,d,e] #change these functions according to choices
for func in functions:
    f2 = np.vectorize(func)
    plt.plot(n, f2(n), label=func.__name__)
plt.legend(loc='best')
plt.show()
