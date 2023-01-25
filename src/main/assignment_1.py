#Nathan Carney
#COT4500, Assignment 1
from decimal import Decimal
import math
A = "0100000001111110101110010000000000000000000000000000000000000000"
c = 0
f = 0
originalSum = 0
counter = 0
for i in range(11, 0, -1):
    if(A[i] == '1'):
        #Since its multiplied by 1,
        #I excluded it here
        c += 2**counter 
    counter += 1 

counter = .5

for i in range(12, 64):
    if(A[i] == '1'):
        f += counter
    counter *= .5

originalSum += (c+f)
if(A[0] == '1'):
    originalSum *= -1


# Problem 1
prob1 = 0
prob1 += 2**(c - 1023)
prob1 *= (f + 1)
print("%.4f\n" % prob1)

# Problem 2
prob2 = math.trunc(prob1)
print("%.1f\n" % prob2)

# Problem 3
prob3 = prob1
prob3 = round(prob3)
print("%.1f\n" % prob3)

# Problem 4
# Absolute Error
prob4a = abs(prob1 - prob3)
prob4a = round(prob4a, 4)
print("%.4f" %prob4a)
# Relative Error
prob4b = abs(Decimal(prob1) - Decimal(prob3)) / abs(Decimal(prob1))
print("%s\n" % prob4b)

# Problem 5
# 1/((n + 1)**3) < 10**(-4)
n = 0 #just for initializing
expr = (1 / ((n + 1)**3) < 10**(-4))
# multipy both sides by their inverses
expr = ((n + 1)**3) > 10**(4) 
# cube both sides
expr = (n + 1) > 10**(4 / 3)
# subtract one
expr = (n > 10**(4/3) - 1)
#since we know n  >  10**(4/3) - 1, 
# going up one integer lets us add the equal sign
expr = (n >= 10**(4 / 3))
n = 10**(4 / 3)
print("%d\n" %n) # minimun number of terms needed to be computed.

# Problem 6 f(x) = x^3 + 4x^2 – 10
#Bisection Method a = (-4), b = (7)
error = 10**(-4)
a = -4
b = 7
def bisection(a, b, error):
    #this is just a formula I found online
    print(math.ceil((math.log2(b - a)-  math.log2(error)) / math.log2(2)))

bisection(a, b, error)
print()

#Newton Raphson Method
def func(x):
    #f(x) = x^3 + 4x^2 – 10
   return x*x*x+4*x*x-10

def derivFunc(x):
    #f'(x) = 3x^2 + 8x
    return 3 * x * x + 8 * x

def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    itr = 0
    while abs(h) >= 0.0001:
        itr += 1
        h = func(x)/derivFunc(x)
        x = x - h
    print(itr)

newtonRaphson(7)
print()
