"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def find_digit(number, digit):
    count=0
    while number!=0:
        last_digit = number%10
        if last_digit==digit:
            count+=1
        number//=10
    return count


n = int(input("Введите количество чисел - "))
digit = int(input("Введите искомую цифру - "))
count=0
count_digit=0
for i in range(n):
    number = int(input("Введите число - "))
    count_digit = find_digit(number,digit)
    count = count + count_digit
print("Цифра {} встречается {} раз".format(digit, count))