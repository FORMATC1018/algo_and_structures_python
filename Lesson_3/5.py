import random
n=int(input("Введите количество чисел в массиве - "))
A = [random.randint(-10,10) for i in range(n)]
print(A)
B = [x for x in A if x<0]
print(B)
maximum = max(B)
for i in range (n):
    if A[i] == maximum:
        print("Максимальный отрицательный элемент {} имеет индекс {}".format(maximum, i))
