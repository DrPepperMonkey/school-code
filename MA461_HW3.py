import math
from typing import List, Tuple
from sympy import *


def choices():
    print('Choose an option below: \n [0]: Biscetion \n [1]: Newton\'s \n [2]: Secant')
    return (int(input()))

def inputs(choice: int):
    dict = []
    if(choice == 0):
        print('Input function.')
        i1 = sympify(input())
        print('Input lower bound.')
        i2 = float(input())
        print('Input uperbound.')
        i3 = float(input())
        print('Input accuracy to nearest decimal.')
        i4 = int(input())
        n = 0
        tmp = [i1, i2, i3, i4, n]
        dict = tmp
    elif(choice == 1):
        print('Input function.')
        i1 = sympify(input())
        print('Input initial guess.')
        i2 = float(input())
        print('Input number of iterations.')
        i3 = int(input())
        tmp = [i1, i2, i3]
        dict = tmp
    elif(choice == 2):
        print('Input function.')
        i1 = sympify(input())
        print('Input First point')
        i2 = float(input())
        print('Input second point.')
        i3 = float(input())
    return dict

def bisection(dict):
    x = symbols('x')
    guess = (dict[1] + dict[2]) / 2
    if ((abs(diff(dict[0]).subs(x, guess))) < (10**(- dict[3]))):
        return (dict[0].subs(x, guess), dict[4])
    else:
        dict[4] = dict[4] + 1
        if ((diff(dict[0]).subs(x, guess)) < 0):
            dict[1] = guess
            return bisection(dict)
        else:
            dict[2] = guess
            return bisection(dict)
    

def newton(dict):
    x = symbols('x')
    der = diff(dict[0])
    guess = dict[1]
    for i in range(dict[2]):
        dict[1] = (guess - (der.subs(x, guess) / diff(der).subs(x, guess)))
    return (dict[0].subs(x, dict[1]))

def secant(dict):
    pass


def main():
    choice = choices()
    dict = inputs(choice)
    if (choice == 0):
        return bisection(dict)
    elif(choice == 1):
        return newton(dict)
    elif(choice == 2):
        pass

print(main())