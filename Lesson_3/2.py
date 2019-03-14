import random
n = int(input("Введите количество чисел в массиве - "))
A = [random.randint(1,100) for i in range(n)]
B = []
print(A)
for i in range(n):
    if A[i]%2 == 0:
        B.append(i)
print(B)