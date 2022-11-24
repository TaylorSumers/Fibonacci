import math

print("Введите n")
n = int(input())
Fn = (pow((1+math.sqrt(5))/2, n) - pow((1-math.sqrt(5))/2, n))/math.sqrt(5)
print("F=", int(Fn))
