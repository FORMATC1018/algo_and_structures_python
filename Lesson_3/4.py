import random
n = int(input("Введите количество чисел в массиве - "))
A = [random.randint(-10,10) for i in range(n)]
print(A)
B=[]
for i in range(n):
    count=1
    for j in range(i+1, n):
        if A[j]==A[i]:
            count+=1
    B.append(count)

maximum = max(B)
C=[]
for i in range(n):
    if B[i] == maximum and maximum>1:
        C.append(i)

if len(C)==0:
    print("Элементы уникальны")
for i in C:
    print ("Элемент {} встречается {} раз".format(A[i], B[i]))
