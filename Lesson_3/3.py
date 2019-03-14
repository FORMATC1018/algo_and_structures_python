import random
n = int(input("Введите количество чисел в массиве - "))
A = [random.randint(-10,10) for i in range(n)]
print(A)
maximum = max(A)
for i in range(n):
    if A[i] == maximum:
        index_max=i
minimum = min(A)
for i in range(n):
    if A[i] == minimum:
        index_min=i
A[index_max], A[index_min] = A[index_min], A[index_max]
print(A)