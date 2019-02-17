n=int(input("Введите число *:"))
d=n/2 # количество шагов для построения треугольника
import math # импорт функции math
g=math.ceil(d) # округление числа, до ближайшего целого
for i in range(0,g):
    for f in range(0,i):
        print(end=" ")
    for j in range(0,2*g-2*i-1):
        print(end="*")
    print("\n")
for i in range(1,g):
    for f in range(0,g-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print(end="*")
    print("\n")
