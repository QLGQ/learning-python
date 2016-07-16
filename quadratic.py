#solving a monadic quadratic equation
import math 
def quadratic(a, b, c):
 if a == 0 and b != 0:
    return none
 elif a != 0:
    s = math.sqrt(b*b-4*a*c) 
    x1 = (-b+s)/(2*a)  
    x2 = (-b-s)/(2*a)
    return x1, x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
