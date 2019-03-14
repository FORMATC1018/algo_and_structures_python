import random
M = int(input("Введите количество столбцов - "))
N = int(input("Введите количество строк - "))
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random.randint(-100,100))
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)