import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import*

X = np.linspace(0,5.2, 100)
h = 0.000000000000001

def f(x):
	return x**3 - 8*x**2 + 17*x - 10
	
def f1(x):
 return (f(x + h)- f(x))/h
 
def F(x):
	return (1/4)*x**4 - (8/3)*x**3 + (17/2)*x**2 -10*x
 
def int(x):
	return quad(f,0,x)
	
def maxmin(n):
	if f1(n)<0:
		print("F(x) has local maximum at x = " + str(n))
	if f1(n)>0:
		print("F(x) has local minimum at x = " + str(n))		
	
def maximum(a, b, c): 
    if (a > b) and (a > c): 
        max = a
    elif (b > a) and (b > c): 
        max = b 
    else: 
        max = c
    return max
    
def minimum(a, b, c): 
    if (a < b) and (a < c): 
        min = a
    elif (b < a) and (b < c): 
        min = b 
    else: 
        min = c
    return min   	
    
#roots of f(x)
coeff = [1, -8, 17, -10]
R = np.roots(coeff)

maxmin(1)
maxmin(2)
maxmin(5)

F_max = maximum(int(1)[0],int(2)[0],int(5)[0])
F_min = minimum(int(1)[0],int(2)[0],int(5)[0])

if F_max<0 and F_min<0 or  F_max>0 and F_min>0 :
	print("F(x) not equals to 0 for all x in (0,5)")

plt.plot(R[0], 0, 'o')
plt.plot(R[1], 0, 'o')
plt.plot(R[2], 0, 'o')
plt.plot(1, F(1), 'o')
plt.plot(2, F(2), 'o')
plt.plot(5, F(5), 'o')
plt.text(1, F(1)*(1-0.1), 'F(1)')
plt.text(2, F(2)*(1-0.1), 'F(2)')
plt.text(5, F(5)*(1-0.05), 'F(5)')
plt.plot(X, f(X), label="f(x)=(x-1)(x-2)(x-5)")
plt.plot(X, F(X), label="F(x)")

plt.legend()
plt.grid()
plt.show()
