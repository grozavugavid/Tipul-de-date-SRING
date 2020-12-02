import math
n=int(input("Introduceti un numar:"))
if n<((10**70)-1):
    r=math.sqrt(n)
    p=int(r)
print(n)
print(n-(p**2))