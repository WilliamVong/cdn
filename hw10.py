import math as Math

def cart_dist(x1, y1, x2, y2):
    return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(cart_dist(1,2,3,4))
print(cart_dist(1,4,3,4))
print(cart_dist(1,2,5,4))

def pyth_triple(a,b,c):
    l=[a,b,c]
    C=max(l)
    l.remove(C)
    B=max(l)
    A=min(l)
    return A**2+B**2==C**2 and A>0 

print(pyth_triple(3,4,5))
print(pyth_triple(3,4,6))
print(pyth_triple(5,12,13))
print(pyth_triple(0,0,1))
print(pyth_triple(Math.sqrt(2),Math.sqrt(2),2))
