import random
n=int(input("Введите количество чисел в массиве - "))
A = [random.randint(-10,10) for i in range(n)]
print(A)
mini = min(A)
maxi = max(A)
for i in range(n):
    if A[i] == mini:
        min_index=i
for j in range(n):
    if A[j] == maxi:
        max_index=j
if min_index<max_index:
        B=[A[i] for i in range(min_index+1, max_index)]
        print(B)
        print("Сумма элементов между минимальным и максимальным - ", sum(B))
elif max_index<min_index:
        B=[A[i] for i in range(max_index+1, min_index)]
        print(B)
        print("Сумма элементов между минимальным и максимальным - ", sum(B))
else:
        print("Максимальный и минимальный элемент стоят рядом")
