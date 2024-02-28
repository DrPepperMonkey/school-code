from sympy import *
from matplotlib import pyplot as plt
import numpy as np
import math

#Provides user with an interface to choose between three options.
#Returns an int for future use
def choices():
    print('Choose an option below: \n [0]: Biscetion \n [1]: Newton\'s \n [2]: Secant')
    return (int(input()))

#Takes the output of choices() and builds and returns an array.
#The array's contents are specifically relevant to the search methods.
def inputs(choice: int):
    dict = []
    if(choice == 0):
        print('Input function.')
        i1 = sympify(input())
        print('Input lower bound.')
        i2 = sympify(input()).evalf()
        print('Input uperbound.')
        i3 = sympify(input()).evalf()
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
        print('Input accuracy to nearest decimal.')
        i4 = int(input())
        tmp = [i1, i2, i3, i4]
        dict = tmp
    return dict

#Option 0 
#Approximates the y value of the lowest point via bisection.
#Returns a float
def bisection(dict):
    x = symbols('x')
    guess = (dict[1] + dict[2]) / 2
    if (dict[0].subs(x, dict[1]) < dict[0].subs(x, guess)):
        return (round(dict[1], 3), round(dict[0].subs(x, dict[1]), 3), 0)
    elif (dict[0].subs(x, dict[2]) < dict[0].subs(x, guess)):
        return (round(dict[2], 3), round(dict[0].subs(x, dict[2]), 3), 0)
    else:
        if ((abs(diff(dict[0]).subs(x, guess))) < (10**(- dict[3]))):
            return (round(guess, 3), round(dict[0].subs(x, guess), 3), dict[4])
        else:
            dict[4] = dict[4] + 1
            if ((diff(dict[0]).subs(x, guess)) < 0):
                dict[1] = guess
                return bisection(dict)
            else:
                dict[2] = guess
                return bisection(dict)
    
#Option 1
#Approximates the y value of lowest point via Newton's method.
#Returns a float.
def newton(dict):
    x = symbols('x')
    der = diff(dict[0])
    guess = dict[1]
    for i in range(dict[2]):
        dict[1] = (guess - (der.subs(x, guess) / diff(der).subs(x, guess)))
    return (dict[1], dict[0].subs(x, dict[1]))

#Option 2
#Approximates the y value of lowest point via Secant method.
#Returns a float.
def secant(dict):
    x = symbols('x')
    der = diff(dict[0])
    if abs(der.subs(x, dict[2])) <= (10**(-dict[3])):
        return (dict[2], dict[0].subs(x, dict[2]))
    else:
        ders1 = der.subs(x, dict[1])
        ders2 = der.subs(x, dict[2])
        tmp = dict[2] - ((dict[2] - dict[1]) / (ders2 - ders1))*(ders2)
        dict[1] = dict[2]
        dict[2] = tmp
        return secant(dict)

def graph(dict, guess: float):
    t = symbols('x')
    x = np.arange(-50, 50, 1)
    y = np.arange(100)
    for i in range(100):
        y[i] = dict[0].subs(t, x[i])
    plt.plot(x, y, label= str(dict[0]))
    xRound = str(guess)
    yRound = str(round((dict[0].subs(t,guess)), 3))
    plt.plot(guess, (dict[0].subs(t, guess)), '.', 
             label='Local Minimizer ' + '(' + xRound + ',' 
             + yRound + ')')
    plt.legend()
    plt.show()


#Main driver function with all the calls.
#Returns the output of one of the three search functions.
def main():
    val = 0.0
    choice = choices()
    dict = inputs(choice)
    if (choice == 0):
        val = bisection(dict)
    elif(choice == 1):
        val = newton(dict)
    elif(choice == 2):
        val = secant(dict)
    graph(dict, val[0])
    print(val)

#Prints the output of the main() function.
main()