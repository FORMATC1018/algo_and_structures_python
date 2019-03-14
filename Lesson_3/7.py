import random
n=int(input("Введите количество чисел в массиве - "))
a = [random.randint(-10,10) for i in range(n)]
print(a)

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
    
for i in range(2,n):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i
        
print("№%3d:%3d" % (min1+1, a[min1]))
print("№%3d:%3d" % (min2+1, a[min2]))
        